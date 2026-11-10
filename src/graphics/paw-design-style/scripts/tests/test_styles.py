"""styles.py: contrast, lock validation, Google Fonts URL, gate refusal."""
import importlib.util
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("styles", SCRIPTS / "styles.py")
st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(st)


def _project(tmp_path, approve_concept=True):
    prod = SCRIPTS / "production.py"
    subprocess.run([sys.executable, str(prod), "init", "--root", str(tmp_path), "--slug", "p", "--title", "P",
                    "--profile", "poster"], check=True, capture_output=True)
    p = tmp_path / "p"
    if approve_concept:
        for cmd in (["start"], ["submit", "--artifact", "x"], ["approve"]):
            subprocess.run([sys.executable, str(prod), cmd[0], "--project", str(p), "concept", *cmd[1:]],
                           check=True, capture_output=True)
    return p


def lock(p, *extra):
    return subprocess.run([sys.executable, str(SCRIPTS / "styles.py"), "lock", "--project", str(p), *extra],
                          capture_output=True, text=True, encoding="utf-8")


def test_ratio_known_values():
    assert st.ratio("#000000", "#FFFFFF") == 21.0
    assert 4.4 < st.ratio("#767676", "#FFFFFF") < 4.6


def test_lock_refuses_while_gate_blocked(tmp_path):
    res = lock(_project(tmp_path, approve_concept=False), "--style", "swiss-grid")
    assert res.returncode == 1 and "concept is pending" in res.stdout


def test_lock_writes_tokens_and_rejects_bad_palette(tmp_path):
    p = _project(tmp_path)
    res = lock(p, "--style", "luxury-serif", "--palette", "ink=#222222")
    assert res.returncode == 1 and "ink on bg" in res.stdout
    res = lock(p, "--style", "luxury-serif")
    assert res.returncode == 0, res.stderr
    css = (p / "style" / "tokens.css").read_text(encoding="utf-8")
    assert "family=Cormorant+Garamond:wght@600;700" in css and "--accent:#C9A45C" in css


def test_google_url_merges_one_family():
    lock_ = {"type": {"display": {"family": "Plus Jakarta Sans", "weights": [800], "source": "google"},
                      "text": {"family": "Plus Jakarta Sans", "weights": [400], "source": "google"}}}
    url = st.google_url(lock_)
    assert url.count("family=") == 1 and "wght@400;800" in url
