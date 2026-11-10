"""copydeck.py: schema, hooks and budgets."""
import importlib.util
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("copydeck", SCRIPTS / "copydeck.py")
cd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cd)

BASE = {"proposition": "x", "goal": "engagement", "hook": {"id": "number-list"},
        "pieces": [{"id": "s01", "role": "cover", "headline": "7 pricing mistakes killing your margin"},
                   {"id": "s02", "role": "body", "headline": "Mistake 1", "body": "Short."},
                   {"id": "s03", "role": "cta", "headline": "Save this", "cta": "Save for later"}]}


def test_clean_carousel():
    fails, warns, _ = cd.validate(BASE, "carousel", 3)
    assert fails == [] and warns == []


def test_piece_count_and_order_warnings():
    deck = {**BASE, "pieces": list(reversed(BASE["pieces"]))}
    _, warns, _ = cd.validate(deck, "carousel", 7)
    assert any("expects 7" in w for w in warns)
    assert any("first piece should be the cover" in w for w in warns)


def test_weak_cta_and_orphan_asterisk():
    deck = {**BASE, "pieces": [{"id": "p01", "role": "single", "headline": "Save 30% on plants*",
                                "cta": "Learn more"}]}
    _, warns, _ = cd.validate(deck, "social-post", 1)
    assert any("generic" in w for w in warns) and any("asterisk" in w for w in warns)
