"""hooks.py: catalog lookups and headline lint."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("hooks", SCRIPTS / "hooks.py")
hooks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hooks)


def test_ids_cover_both_kinds():
    ids = hooks.ids()
    assert ids["number-list"] == "headline" and ids["scale-contrast"] == "visual"


def test_lint_word_band_is_a_fail():
    res = hooks.lint("Our brand new extended winter collection is finally here for everyone", "poster")
    assert not res["ok"] and "Cut words" in res["fails"][0]


def test_lint_clean_number_headline():
    res = hooks.lint("7 pricing mistakes killing your margin", "carousel-cover")
    assert res["ok"] and not res["warns"] and res["has_number"]


def test_event_without_weekday_gets_a_note():
    res = hooks.lint("Night Market 14 March", "poster", "event")
    assert any("weekday" in n for n in res["notes"])
