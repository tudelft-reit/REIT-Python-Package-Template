import subprocess
from pathlib import Path

from context import ContextUpdater
from jinja2.sandbox import SandboxedEnvironment
import pytest

REMOTE_URL = "https://gitlab.ewi.tudelft.nl/reit/test-repo.git"


def git(*args: str, cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def create_repo(path: Path, files: list[str]) -> Path:
    path.mkdir()
    git("init", cwd=path)
    git("remote", "add", "origin", REMOTE_URL, cwd=path)
    for file in files:
        (path / file).parent.mkdir(parents=True, exist_ok=True)
        (path / file).write_text("content")
    if files:
        git("add", "--all", cwd=path)
        git("commit", "--message", "Initial commit", cwd=path)
    return path


@pytest.fixture(autouse=True)
def git_identity(monkeypatch: pytest.MonkeyPatch) -> None:
    # Do not depend on the git config of the machine running the tests
    monkeypatch.setenv("GIT_CONFIG_GLOBAL", "/dev/null")
    monkeypatch.setenv("GIT_CONFIG_COUNT", "2")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "user.name")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", "Python Template")
    monkeypatch.setenv("GIT_CONFIG_KEY_1", "user.email")
    monkeypatch.setenv("GIT_CONFIG_VALUE_1", "python-template@tudelft.nl")


@pytest.fixture
def context_updater() -> ContextUpdater:
    return ContextUpdater(SandboxedEnvironment())


def prompt_context(dst_path: Path) -> dict:
    return {"_copier_phase": "prompt", "_copier_conf": {"dst_path": str(dst_path)}}


@pytest.mark.parametrize(
    ("files", "expected"),
    [
        ([], True),
        (["README.md"], True),
        (["LICENSE"], True),
        ([".gitignore"], True),
        (["README.md", "LICENSE", ".gitignore"], True),
        (["readme.md"], False),
        (["README.rst"], False),
        (["LICENSE.txt"], False),
        (["main.py"], False),
        (["README.md", "main.py"], False),
        (["README.md", "LICENSE", ".gitignore", "pyproject.toml"], False),
        (["docs/README.md"], False),
    ],
)
def test_check_is_new_project(
    context_updater: ContextUpdater, tmp_path: Path, files: list[str], expected: bool
) -> None:
    repo = create_repo(tmp_path / "repo", files)
    assert context_updater._check_is_new_project(repo) is expected


def test_cloned_empty_repository_is_new_project(context_updater: ContextUpdater, tmp_path: Path) -> None:
    remote = tmp_path / "remote.git"
    git("init", "--bare", str(remote), cwd=tmp_path)
    git("clone", str(remote), "clone", cwd=tmp_path)
    assert context_updater._check_is_new_project(tmp_path / "clone")


def test_hook_new_project(context_updater: ContextUpdater, tmp_path: Path) -> None:
    repo = create_repo(tmp_path / "repo", ["README.md", "LICENSE"])
    context = context_updater.hook(prompt_context(repo))
    assert context["is_new_project"] is True
    assert context["host"] == "gitlab.ewi.tudelft.nl"
    assert context["url"] == "https://gitlab.ewi.tudelft.nl/reit/test-repo"
    assert context["repo_project_name"] == "test-repo"


def test_hook_uncommitted_changes_exits(context_updater: ContextUpdater, tmp_path: Path) -> None:
    repo = create_repo(tmp_path / "repo", ["README.md"])
    (repo / "README.md").write_text("changed")
    with pytest.raises(SystemExit):
        context_updater.hook(prompt_context(repo))
