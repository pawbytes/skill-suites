#!/usr/bin/env python3
"""Unit tests for merge-config.py"""
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

# Load the module with hyphen in filename
script_path = Path(__file__).parent.parent / "merge-config.py"
spec = importlib.util.spec_from_file_location("merge_config", script_path)
mc = importlib.util.module_from_spec(spec)
sys.modules["merge_config"] = mc

# Mock yaml for testing if not available
try:
    spec.loader.exec_module(mc)
except ImportError:
    # Create a mock yaml module
    import types
    yaml_mock = types.ModuleType("yaml")

    def safe_load(s):
        import yaml
        return yaml.safe_load(s)

    def dump(data, f, **kwargs):
        import yaml
        return yaml.dump(data, f, **kwargs)

    yaml_mock.safe_load = safe_load
    yaml_mock.dump = dump
    sys.modules["yaml"] = yaml_mock
    spec.loader.exec_module(mc)


class TestCoreKeys:
    """Tests for core keys constants."""

    def test_core_keys_exist(self):
        """Should have core keys defined."""
        assert hasattr(mc, "_CORE_KEYS")
        assert "user_name" in mc._CORE_KEYS
        assert "communication_language" in mc._CORE_KEYS


class TestExtractModuleMetadata:
    """Tests for extract_module_metadata function."""

    def test_extracts_name(self):
        """Should extract name from module yaml."""
        module_yaml = {"name": "Test Module", "code": "test"}
        result = mc.extract_module_metadata(module_yaml)
        assert result["name"] == "Test Module"

    def test_extracts_description(self):
        """Should extract description from module yaml."""
        module_yaml = {"description": "A test module", "code": "test"}
        result = mc.extract_module_metadata(module_yaml)
        assert result["description"] == "A test module"

    def test_handles_missing_fields(self):
        """Should handle missing optional fields."""
        module_yaml = {"code": "test"}
        result = mc.extract_module_metadata(module_yaml)
        assert "name" not in result


class TestApplyResultTemplates:
    """Tests for apply_result_templates function."""

    def test_no_template_passthrough(self):
        """Should pass through values without templates."""
        module_yaml = {}
        answers = {"key": "value"}
        result = mc.apply_result_templates(module_yaml, answers, verbose=False)
        assert result["key"] == "value"

    def test_applies_template(self):
        """Should apply result template."""
        module_yaml = {
            "path_var": {
                "result": "{project-root}/custom/{value}"
            }
        }
        answers = {"path_var": "myfolder"}
        result = mc.apply_result_templates(module_yaml, answers, verbose=False)
        assert "{project-root}" in result["path_var"]
        assert "myfolder" in result["path_var"]


class TestExtractUserSettings:
    """Tests for extract_user_settings function."""

    def test_extracts_user_name(self):
        """Should extract user_name from core answers."""
        module_yaml = {}
        answers = {"core": {"user_name": "John"}}
        result = mc.extract_user_settings(module_yaml, answers)
        assert result["user_name"] == "John"

    def test_extracts_communication_language(self):
        """Should extract communication_language from core answers."""
        module_yaml = {}
        answers = {"core": {"communication_language": "en"}}
        result = mc.extract_user_settings(module_yaml, answers)
        assert result["communication_language"] == "en"

    def test_extracts_user_setting_vars(self):
        """Should extract module vars with user_setting: true."""
        module_yaml = {
            "my_var": {"user_setting": True}
        }
        answers = {"module": {"my_var": "value"}}
        result = mc.extract_user_settings(module_yaml, answers)
        assert result["my_var"] == "value"


class TestLoadJsonFile:
    """Tests for load_json_file function."""

    def test_loads_valid_json(self):
        """Should load valid JSON file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump({"key": "value"}, f)
            f.flush()
            result = mc.load_json_file(f.name)
        assert result["key"] == "value"


def run_tests():
    """Run all tests and report results."""
    test_classes = [
        TestCoreKeys,
        TestExtractModuleMetadata,
        TestApplyResultTemplates,
        TestExtractUserSettings,
        TestLoadJsonFile,
    ]

    passed = 0
    failed = 0

    for test_class in test_classes:
        instance = test_class()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                try:
                    getattr(instance, method_name)()
                    passed += 1
                    print(f"PASS: {test_class.__name__}.{method_name}")
                except AssertionError as e:
                    failed += 1
                    print(f"FAIL: {test_class.__name__}.{method_name}")
                    print(f"  {e}")

    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed")
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)