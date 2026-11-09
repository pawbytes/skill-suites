"""merge-config.py validates module answers against module.yaml `choices` and `type`.

Kept apart from test_merge_config.py, which stays identical to the sibling suites' copy.
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import yaml

SCRIPTS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("merge_config_v", SCRIPTS / "merge-config.py")
mc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mc)
MODULE_YAML = SCRIPTS.parent / "assets" / "module.yaml"
MODULE = yaml.safe_load(MODULE_YAML.read_text(encoding="utf-8"))


def test_module_yaml_declares_choices_and_types():
    assert MODULE["default_profile"]["choices"][0] == "social-post" and len(MODULE["default_profile"]["choices"]) == 8
    assert MODULE["default_budget_usd"]["type"] == "positive_number"
    assert MODULE["takes_per_image"]["type"] == "positive_integer"


def test_defaults_pass_their_own_validation():
    defaults = {k: v["default"] for k, v in MODULE.items() if isinstance(v, dict) and "default" in v}
    _, problems = mc.validate_module_answers(MODULE, defaults)
    assert problems == []


def test_bad_answers_are_named():
    _, problems = mc.validate_module_answers(MODULE, {
        "default_profile": "billboard", "image_provider": "cloud", "default_budget_usd": -5,
        "takes_per_image": 1.5, "codex_path": ""})
    text = " | ".join(problems)
    assert "default_profile: 'billboard'" in text and "image_provider: 'cloud'" in text
    assert "default_budget_usd: -5 must be greater than 0" in text
    assert "takes_per_image: 1.5 must be a whole number" in text
    assert "codex_path" not in text


def test_numeric_strings_are_converted():
    checked, problems = mc.validate_module_answers(MODULE, {"default_budget_usd": "50", "takes_per_image": "3"})
    assert problems == [] and checked == {"default_budget_usd": 50, "takes_per_image": 3}
    _, problems = mc.validate_module_answers(MODULE, {"default_budget_usd": "lots"})
    assert problems == ["default_budget_usd: 'lots' is not a number"]


def test_cli_exits_1_and_writes_nothing_on_bad_answers(tmp_path):
    answers = tmp_path / "answers.json"
    answers.write_text(json.dumps({"module": {"default_profile": "billboard"}}), encoding="utf-8")
    config = tmp_path / "config.yaml"
    proc = subprocess.run([sys.executable, str(SCRIPTS / "merge-config.py"), "--config-path", str(config),
                           "--user-config-path", str(tmp_path / "config.user.yaml"), "--module-yaml",
                           str(MODULE_YAML), "--answers", str(answers)], capture_output=True, text=True,
                          encoding="utf-8")
    assert proc.returncode == 1
    assert "default_profile" in json.loads(proc.stderr)["problems"][0]
    assert not config.exists()


def test_cli_writes_converted_numbers(tmp_path):
    answers = tmp_path / "answers.json"
    answers.write_text(json.dumps({"module": {"default_budget_usd": "40", "default_profile": "carousel"}}),
                       encoding="utf-8")
    config = tmp_path / "config.yaml"
    proc = subprocess.run([sys.executable, str(SCRIPTS / "merge-config.py"), "--config-path", str(config),
                           "--user-config-path", str(tmp_path / "config.user.yaml"), "--module-yaml",
                           str(MODULE_YAML), "--answers", str(answers)], capture_output=True, text=True,
                          encoding="utf-8")
    assert proc.returncode == 0, proc.stderr
    design = yaml.safe_load(config.read_text(encoding="utf-8"))["design"]
    assert design["default_budget_usd"] == 40 and design["default_profile"] == "carousel"


def test_image_provider_and_codex_path_are_user_settings():
    assert MODULE["image_provider"]["choices"] == ["fal", "codex-cli"]
    assert MODULE["image_provider"]["default"] == "fal"
    assert MODULE["image_provider"]["user_setting"] is True and MODULE["codex_path"]["user_setting"] is True
    assert MODULE["codex_path"]["default"] == ""
    _, problems = mc.validate_module_answers(MODULE, {"image_provider": "midjourney"})
    assert problems == ["image_provider: 'midjourney' is not one of fal, codex-cli"]
    settings = mc.extract_user_settings(MODULE, {"module": {"image_provider": "codex-cli", "codex_path": "C:/x/codex.exe"}})
    assert settings == {"image_provider": "codex-cli", "codex_path": "C:/x/codex.exe"}
