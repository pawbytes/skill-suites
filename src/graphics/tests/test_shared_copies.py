"""Every bundled copy of a shared file matches the canonical one in _shared/."""
from conftest import SUITE, load

sync = load(SUITE / "_shared" / "sync.py", "design_sync")


def test_copies_identical():
    drift = [str(dest) for src, dest in sync.plan() if not dest.is_file() or dest.read_bytes() != src.read_bytes()]
    assert not drift, f"shared copies drifted; run `uv run src/graphics/_shared/sync.py`: {drift}"


def test_every_listed_skill_exists():
    missing = [s for skills in sync.COPIES.values() for s in skills if not (SUITE / s).is_dir()]
    assert not missing, f"skills listed in sync.py are missing: {missing}"


def test_every_bundled_import_is_bundled():
    """A script that imports a sibling module must find it in its own skill folder."""
    imports = {"fal.py": ["production"], "codex_image.py": ["production"], "qc.py": ["specs"],
               "frames.py": ["specs"]}
    problems = []
    for script, deps in imports.items():
        for skill in sync.COPIES[f"scripts/{script}"]:
            for dep in deps:
                if not (SUITE / skill / "scripts" / f"{dep}.py").is_file():
                    problems.append(f"{skill}: {script} needs {dep}.py")
    assert not problems, problems
