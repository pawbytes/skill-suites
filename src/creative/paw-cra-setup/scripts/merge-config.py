#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Merge module configuration into shared .pawbytes/config/config.yaml and config.user.yaml.

Reads a module.yaml definition and a JSON answers file, then writes or updates
the shared config.yaml (core values at root + module section) and config.user.yaml
(user_name, communication_language, plus any module variable with user_setting: true).
Uses an anti-zombie pattern for the module section in config.yaml.

Exit codes: 0=success, 1=validation error, 2=runtime error
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: pyyaml is required (PEP 723 dependency)", file=sys.stderr)
    sys.exit(2)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Merge module config into shared .pawbytes/config/config.yaml with anti-zombie pattern."
    )
    parser.add_argument(
        "--config-path",
        required=True,
        help="Path to the target config.yaml file",
    )
    parser.add_argument(
        "--module-yaml",
        required=True,
        help="Path to the module.yaml definition file",
    )
    parser.add_argument(
        "--answers",
        required=True,
        help="Path to JSON file with collected answers",
    )
    parser.add_argument(
        "--user-config-path",
        required=True,
        help="Path to the target config.user.yaml file",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed progress to stderr",
    )
    return parser.parse_args()


def load_yaml_file(path: str) -> dict:
    """Load a YAML file, returning empty dict if file doesn't exist."""
    file_path = Path(path)
    if not file_path.exists():
        return {}
    with open(file_path, "r", encoding="utf-8") as f:
        content = yaml.safe_load(f)
    return content if content else {}


def load_json_file(path: str) -> dict:
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# Keys that live at config root (shared across all modules)
_CORE_KEYS = frozenset(
    {"user_name", "communication_language", "document_output_language", "output_directory"}
)

# Core keys that are always written to config.user.yaml
_CORE_USER_KEYS = ("user_name", "communication_language")


def extract_module_metadata(module_yaml: dict) -> dict:
    """Extract non-variable metadata fields from module.yaml."""
    meta = {}
    for k in ("name", "description", "version"):
        if k in module_yaml:
            meta[k] = module_yaml[k]
    return meta


def apply_result_templates(
    module_yaml: dict, module_answers: dict, verbose: bool = False
) -> dict:
    """Apply result templates from module.yaml to transform raw answer values.

    For each answer, if the corresponding variable definition in module.yaml has
    a 'result_template' field, replaces {value} in that template with the answer.
    Skips the template if the answer already contains '{project-root}' to prevent
    double-prefixing.
    """
    questions = module_yaml.get("questions", [])
    transformed = {}

    # Build a lookup from key to question definition
    question_lookup = {q.get("key"): q for q in questions if isinstance(q, dict)}

    for key, value in module_answers.items():
        var_def = question_lookup.get(key)
        if (
            isinstance(var_def, dict)
            and "result_template" in var_def
            and "{project-root}" not in str(value)
        ):
            template = var_def["result_template"]
            transformed[key] = template.replace("{value}", str(value))
            if verbose:
                print(
                    f"Applied result template for '{key}': {value} -> {transformed[key]}",
                    file=sys.stderr,
                )
        else:
            transformed[key] = value
    return transformed


def merge_config(
    existing_config: dict,
    module_yaml: dict,
    answers: dict,
    verbose: bool = False,
) -> dict:
    """Merge answers into config, applying anti-zombie pattern.

    Args:
        existing_config: Current config.yaml contents (may be empty)
        module_yaml: The module definition
        answers: JSON with 'core' and/or 'module' keys
        verbose: Print progress to stderr

    Returns:
        Updated config dict ready to write
    """
    config = dict(existing_config)
    module_code = module_yaml.get("code")

    if not module_code:
        print("Error: module.yaml must have a 'code' field", file=sys.stderr)
        sys.exit(1)

    # Strip user-only keys from config — they belong exclusively in config.user.yaml
    for key in _CORE_USER_KEYS:
        if key in config:
            if verbose:
                print(f"Removing user-only key '{key}' from config (belongs in config.user.yaml)", file=sys.stderr)
            del config[key]

    # Write core values at root (global properties)
    # Exclude user-only keys — those belong exclusively in config.user.yaml
    core_answers = answers.get("core")
    if core_answers:
        shared_core = {k: v for k, v in core_answers.items() if k not in _CORE_USER_KEYS}
        if shared_core:
            if verbose:
                print(f"Writing core config at root: {list(shared_core.keys())}", file=sys.stderr)
            config.update(shared_core)

    # Anti-zombie: remove existing module section
    if module_code in config:
        if verbose:
            print(
                f"Removing existing '{module_code}' section (anti-zombie)",
                file=sys.stderr,
            )
        del config[module_code]

    # Build module section: metadata + variable values
    module_section = extract_module_metadata(module_yaml)
    module_answers = apply_result_templates(
        module_yaml, answers.get("module", {}), verbose
    )
    module_section.update(module_answers)

    if verbose:
        print(
            f"Writing '{module_code}' section with keys: {list(module_section.keys())}",
            file=sys.stderr,
        )

    config[module_code] = module_section

    return config


def extract_user_settings(module_yaml: dict, answers: dict) -> dict:
    """Collect settings that belong in config.user.yaml.

    Includes user_name and communication_language from core answers, plus any
    module variable whose definition contains user_setting: true.
    """
    user_settings = {}

    core_answers = answers.get("core", {})
    for key in _CORE_USER_KEYS:
        if key in core_answers:
            user_settings[key] = core_answers[key]

    module_answers = answers.get("module", {})
    questions = module_yaml.get("questions", [])

    for question in questions:
        if isinstance(question, dict) and question.get("user_setting") is True:
            var_name = question.get("key")
            if var_name and var_name in module_answers:
                user_settings[var_name] = module_answers[var_name]

    return user_settings


def write_config(config: dict, config_path: str, verbose: bool = False) -> None:
    """Write config dict to YAML file, creating parent dirs as needed."""
    path = Path(config_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"Writing config to {path}", file=sys.stderr)

    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(
            config,
            f,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
        )


def main():
    args = parse_args()

    # Load inputs
    module_yaml = load_yaml_file(args.module_yaml)
    if not module_yaml:
        print(f"Error: Could not load module.yaml from {args.module_yaml}", file=sys.stderr)
        sys.exit(1)

    answers = load_json_file(args.answers)
    existing_config = load_yaml_file(args.config_path)

    if args.verbose:
        exists = Path(args.config_path).exists()
        print(f"Config file exists: {exists}", file=sys.stderr)
        if exists:
            print(f"Existing sections: {list(existing_config.keys())}", file=sys.stderr)

    # Merge and write config.yaml
    updated_config = merge_config(existing_config, module_yaml, answers, args.verbose)
    write_config(updated_config, args.config_path, args.verbose)

    # Merge and write config.user.yaml
    user_settings = extract_user_settings(module_yaml, answers)
    existing_user_config = load_yaml_file(args.user_config_path)

    # Anti-zombie for user config: remove existing module keys
    module_code = module_yaml.get("code")
    questions = module_yaml.get("questions", [])
    module_user_keys = [q.get("key") for q in questions if isinstance(q, dict) and q.get("user_setting") is True]

    updated_user_config = dict(existing_user_config)
    for key in module_user_keys:
        if key in updated_user_config:
            del updated_user_config[key]

    updated_user_config.update(user_settings)
    if user_settings:
        write_config(updated_user_config, args.user_config_path, args.verbose)

    # Output result summary as JSON
    result = {
        "status": "success",
        "config_path": str(Path(args.config_path).resolve()),
        "user_config_path": str(Path(args.user_config_path).resolve()),
        "module_code": module_code,
        "core_updated": bool(answers.get("core")),
        "module_keys": list(updated_config.get(module_code, {}).keys()),
        "user_keys": list(user_settings.keys()),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()