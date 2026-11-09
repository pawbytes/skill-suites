"""production.py: profiles, gates, skips, reopen, budget."""
import json
import subprocess
import sys

import pytest

from conftest import SHARED, load

production = load(SHARED / "production.py", "design_production")
specs = load(SHARED / "specs.py", "design_specs")


def run(*args):
    p = subprocess.run([sys.executable, str(SHARED / "production.py"), *args], capture_output=True, text=True,
                       encoding="utf-8")
    return p.returncode, json.loads(p.stdout or p.stderr)


@pytest.fixture
def project(tmp_path):
    code, res = run("init", "--root", str(tmp_path), "--slug", "demo", "--title", "Demo", "--profile", "carousel",
                    "--budget", "1")
    assert code == 0, res
    return tmp_path / "demo"


def test_every_profile_placement_is_in_the_catalog():
    for name, prof in production.PROFILES.items():
        for pid in prof["placements"]:
            assert pid in specs.load()["placements"], f"{name}: {pid}"


def test_init_creates_folders_and_defaults(project):
    data = json.loads((project / "production.json").read_text(encoding="utf-8"))
    assert data["pieces"] == 7 and data["placements"] == ["instagram-feed-portrait"]
    assert all(s["status"] == "pending" for s in data["stages"].values())
    for d in production.PROJECT_DIRS:
        assert (project / d).is_dir()


def test_gate_order_and_approval_flow(project):
    code, res = run("start", "--project", str(project), "style")
    assert code == 1 and "concept is pending" in res["reasons"][0]
    assert run("start", "--project", str(project), "concept")[0] == 0
    code, res = run("approve", "--project", str(project), "concept")
    assert code == 2 and "submit an artifact" in res["error"]
    assert run("submit", "--project", str(project), "concept", "--artifact", "concept/copy.json")[0] == 0
    assert run("approve", "--project", str(project), "concept")[0] == 0
    assert run("gate", "--project", str(project), "style")[0] == 0


def test_compose_cannot_be_skipped_but_imagery_can(project):
    assert run("skip", "--project", str(project), "imagery", "--reason", "type-only")[0] == 0
    code, res = run("skip", "--project", str(project), "compose", "--reason", "no")
    assert code == 2 and "cannot be skipped" in res["error"]
    assert run("enable", "--project", str(project), "imagery")[0] == 0


def test_reopen_stales_downstream(project):
    for st in ("concept", "style"):
        run("start", "--project", str(project), st)
        run("submit", "--project", str(project), st, "--artifact", "x")
        run("approve", "--project", str(project), st)
    code, res = run("reopen", "--project", str(project), "concept")
    assert code == 0 and res["staled"] == ["style"]


def test_budget_check_and_ack(project):
    assert production.budget_check(project, 0.5) == []
    production.log_cost(project, "imagery", "fal-ai/x", 0.8)
    assert production.budget_check(project, 0.5)
    run("ack-budget", "--project", str(project), "--reason", "more takes", "--cap-usd", "3")
    assert production.budget_check(project, 0.5) == []


def test_set_validates(project):
    code, res = run("set", "--project", str(project), "pieces=25")
    assert code == 2 and "between 1 and 20" in res["error"]
    code, res = run("set", "--project", str(project), "placements=instagram-story,tiktok-photo", "medium=digital")
    assert code == 0 and res["changed"]["placements"] == ["instagram-story", "tiktok-photo"]
