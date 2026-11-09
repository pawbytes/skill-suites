"""Catalogs and contracts agree with each other: specs, styles, pairings, hooks, help rows, skills."""
import csv
import json
import re

from conftest import SHARED, SUITE, load

specs = load(SHARED / "specs.py", "design_specs_c")
styles = load(SUITE / "paw-design-style" / "scripts" / "styles.py", "design_styles")
hooks = load(SUITE / "paw-design-concept" / "scripts" / "hooks.py", "design_hooks")


def test_every_placement_is_complete():
    data = specs.load()
    classes = data["rules"]["classes"]
    for pid, e in data["placements"].items():
        assert re.fullmatch(r"[a-z0-9-]+", pid)
        assert e["class"] in classes, pid
        if e["unit"] == "mm":
            assert e["w_mm"] > 0 and e["h_mm"] > 0 and e["bleed_mm"] >= 0 and e["dpi"] >= 100, pid
        else:
            assert e["w"] > 0 and e["h"] > 0, pid
            if e["safe_zone"]:
                l, t, r, b = specs.safe_rect(e, data)
                assert r - l > e["w"] * 0.25 and b - t > e["h"] * 0.25, f"{pid}: safe zone leaves too little"
        assert e["formats"], pid


def test_aliases_are_unique():
    seen = {}
    for pid, e in specs.load()["placements"].items():
        for al in e.get("aliases", []):
            assert al not in seen, f"alias {al} on {pid} and {seen.get(al)}"
            seen[al] = pid


def test_styles_reference_real_pairings_and_pass_contrast():
    pair_ids = {p["id"] for p in styles.pairings()}
    ids = set()
    for s in styles.styles():
        assert s["id"] not in ids
        ids.add(s["id"])
        assert s["pairing"] in pair_ids and all(p in pair_ids for p in s["alt_pairings"])
        for fg, bg, need in styles.PAIRS:
            assert styles.ratio(s["palette"][fg], s["palette"][bg]) >= need, f"{s['id']} {fg}/{bg}"
        assert s["imagery"]["kind"] in styles.KINDS


def test_hook_ids_unique_and_tagged():
    data = hooks.load()
    ids = [h["id"] for h in data["headline"]] + [v["id"] for v in data["visual"]]
    assert len(ids) == len(set(ids))
    for h in data["headline"]:
        assert set(h["goals"]) <= set(hooks.GOALS) and set(h["formats"]) <= set(hooks.FORMATS), h["id"]
    for v in data["visual"]:
        assert set(v["goals"]) <= set(hooks.GOALS) and set(v["formats"]) <= set(hooks.FORMATS), v["id"]


def test_help_rows_name_real_skills():
    rows = list(csv.DictReader((SUITE / "paw-design-setup" / "assets" / "module-help.csv").open(encoding="utf-8")))
    names = {r["skill"] for r in rows}
    skills = {p.name for p in SUITE.iterdir() if (p / "SKILL.md").is_file()}
    assert names == skills, names ^ skills
    for r in rows:
        for ref in filter(None, [r["after"], r["before"]]):
            assert ref.split(":")[0] in skills, ref


def test_skill_frontmatter_and_references_exist():
    for skill in (p for p in SUITE.iterdir() if (p / "SKILL.md").is_file()):
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        m = re.match(r'---\nname: (\S+)\ndescription: "(.+)"\n---\n', text)
        assert m and m.group(1) == skill.name, skill.name
        assert len(m.group(2)) <= 1024
        for ref in set(re.findall(r"`(references/[\w.-]+\.md)`", text)):
            assert (skill / ref).is_file(), f"{skill.name}: {ref}"
        for script in set(re.findall(r"scripts/([\w-]+\.py)", text)):
            assert (skill / "scripts" / script).is_file(), f"{skill.name}: scripts/{script}"


def test_trigger_sets_exist_and_parse():
    for skill in (p for p in SUITE.iterdir() if (p / "SKILL.md").is_file()):
        data = json.loads((skill / "evals" / "triggers.json").read_text(encoding="utf-8"))
        assert any(q["should_trigger"] for q in data) and any(not q["should_trigger"] for q in data), skill.name
