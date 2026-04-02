"""Tests for parse_commits.py"""

import pytest
from parse_commits import (
    parse_commit_message,
    determine_version_bump,
    group_commits,
    CommitType,
    Commit,
)


class TestParseCommitMessage:
    """Tests for commit message parsing."""

    def test_simple_feat(self):
        """Test simple feature commit."""
        commit = parse_commit_message("feat: add new feature")
        assert commit.type == CommitType.FEAT
        assert commit.scope is None
        assert commit.breaking is False
        assert commit.description == "add new feature"

    def test_feat_with_scope(self):
        """Test feature commit with scope."""
        commit = parse_commit_message("feat(api): add new endpoint")
        assert commit.type == CommitType.FEAT
        assert commit.scope == "api"
        assert commit.description == "add new endpoint"

    def test_fix(self):
        """Test fix commit."""
        commit = parse_commit_message("fix: resolve null pointer issue")
        assert commit.type == CommitType.FIX
        assert commit.description == "resolve null pointer issue"

    def test_breaking_with_exclamation(self):
        """Test breaking change with exclamation mark."""
        commit = parse_commit_message("feat!: remove deprecated API")
        assert commit.type == CommitType.BREAKING
        assert commit.breaking is True
        assert commit.description == "remove deprecated API"

    def test_breaking_with_scope(self):
        """Test breaking change with scope."""
        commit = parse_commit_message("feat(api)!: change response format")
        assert commit.type == CommitType.BREAKING
        assert commit.scope == "api"
        assert commit.breaking is True

    def test_explicit_breaking_type(self):
        """Test explicit 'breaking' type."""
        commit = parse_commit_message("breaking: remove old interface")
        assert commit.type == CommitType.BREAKING
        assert commit.breaking is True

    def test_pr_number_extraction(self):
        """Test PR number extraction from commit."""
        commit = parse_commit_message("feat: add feature (#123)")
        assert commit.pr_number == "123"
        assert commit.description == "add feature (#123)"

    def test_non_conventional_commit(self):
        """Test handling of non-conventional commit."""
        commit = parse_commit_message("update the configuration file")
        assert commit.type == CommitType.OTHER
        assert commit.description == "update the configuration file"

    def test_various_types(self):
        """Test various commit types."""
        types = {
            "docs": CommitType.DOCS,
            "style": CommitType.STYLE,
            "refactor": CommitType.REFACTOR,
            "perf": CommitType.PERF,
            "test": CommitType.TEST,
            "build": CommitType.BUILD,
            "ci": CommitType.CI,
            "chore": CommitType.CHORE,
            "revert": CommitType.REVERT,
        }
        for prefix, expected_type in types.items():
            commit = parse_commit_message(f"{prefix}: some change")
            assert commit.type == expected_type


class TestDetermineVersionBump:
    """Tests for version bump determination."""

    def test_major_bump(self):
        """Test major version bump for breaking changes."""
        commits = [
            Commit("abc123", CommitType.BREAKING, None, True, "break API", "feat!: break API"),
            Commit("def456", CommitType.FEAT, None, False, "add feature", "feat: add feature"),
        ]
        assert determine_version_bump(commits) == "major"

    def test_minor_bump(self):
        """Test minor version bump for features."""
        commits = [
            Commit("abc123", CommitType.FEAT, None, False, "add feature", "feat: add feature"),
            Commit("def456", CommitType.FIX, None, False, "fix bug", "fix: fix bug"),
        ]
        assert determine_version_bump(commits) == "minor"

    def test_patch_bump(self):
        """Test patch version bump for fixes only."""
        commits = [
            Commit("abc123", CommitType.FIX, None, False, "fix bug", "fix: fix bug"),
            Commit("def456", CommitType.DOCS, None, False, "update docs", "docs: update docs"),
        ]
        assert determine_version_bump(commits) == "patch"

    def test_empty_commits(self):
        """Test patch bump when no commits."""
        assert determine_version_bump([]) == "patch"


class TestGroupCommits:
    """Tests for commit grouping."""

    def test_grouping(self):
        """Test commits are grouped correctly."""
        commits = [
            Commit("a1", CommitType.FEAT, None, False, "feat1", "feat: feat1"),
            Commit("a2", CommitType.FEAT, None, False, "feat2", "feat: feat2"),
            Commit("b1", CommitType.FIX, None, False, "fix1", "fix: fix1"),
        ]
        grouped = group_commits(commits)

        assert CommitType.FEAT in grouped
        assert CommitType.FIX in grouped
        assert len(grouped[CommitType.FEAT]) == 2
        assert len(grouped[CommitType.FIX]) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])