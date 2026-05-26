import subprocess
from pathlib import Path

from copier import __version__ as copier_version
from copier_templates_extensions import ContextHook
import giturlparse
from jinja2.sandbox import SandboxedEnvironment
from packaging.version import Version


class ContextUpdater(ContextHook):
    def __init__(self, environment: SandboxedEnvironment):
        super().__init__(environment)

        if Version(copier_version) < Version("9.6.0"):
            # Version 9.6 is needed for context["_copier_phase"]
            print("Update copier to version 9.6 or later")
            exit(-1)

        self._run_git(
            ["help"],
            error_message="Git does not seem to be installed. Please install it and try again.",
        )

        _, git_user_name = self._run_git(
            ["config", "user.name"],
            error_message="Configure the git user.name and try again.",
        )
        if git_user_name == "":
            print("Configure the git user.name and try again.")
            exit(-1)

        _, git_user_email = self._run_git(
            ["config", "user.email"],
            error_message="Configure the git user.email and try again.",
        )
        if git_user_email == "":
            print("Configure the git user.email and try again.")
            exit(-1)

        self.is_new_project: bool | None = None
        self.is_python3_13_or_later: bool | None = None
        self.given_name: str | None = None
        self.family_name: str | None = None
        self.host: str | None = None
        self.url: str | None = None
        self.repo_project_name: str | None = None

    @staticmethod
    def _run_git(
        args: list[str],
        cwd: Path | None = None,
        error_message: str | None = None,
        allow_error: bool = False,
    ) -> tuple[int, str]:
        ret = subprocess.run(["git", *args], capture_output=True, cwd=cwd)
        stdout = ret.stdout.decode("utf-8").strip()
        if ret.returncode != 0 and not allow_error:
            print(error_message or f"Running 'git {' '.join(args)}' failed.")
            exit(-1)
        return ret.returncode, stdout

    def _check_is_valid_git_repository(self, dst_path: Path) -> None:
            if not dst_path.exists():
                print(
                    "Destination path does not exist. First create an empty repository online, "
                    "clone it locally, then run Copier in that folder."
                )
                exit(-1)

            _, status_porcelain = self._run_git(
                ["status", "--porcelain"],
                cwd=dst_path,
                error_message=(
                    f"Running 'git status' in '{dst_path}' failed. "
                    "Please run this template in a cloned git repository."
                ),
            )

            if status_porcelain != "":
                print(
                    "The repository has uncommitted changes. "
                    "Please commit or stash them before proceeding."
                )
                exit(-1)

    def _get_parsed_git_url(self, dst_path: Path) -> giturlparse.GitUrlParsed:
        _, origin_remote = self._run_git(
            ["remote", "get-url", "origin"],
            cwd=dst_path,
            error_message=(
                "Could not find git remote 'origin'. "
                "Create an empty repository online, clone it, then run copier in that folder."
            ),
        )

        parsed_url = giturlparse.parse(origin_remote)
        if parsed_url is None:
            print(f"Could not parse repository remote URL: '{origin_remote}'")
            exit(-1)

        return parsed_url

    def hook(self, context: dict) -> dict:
        if self.is_new_project is None and context["_copier_phase"] == "prompt":
            dst_path = Path(context["_copier_conf"]["dst_path"]).resolve()
            self._check_is_valid_git_repository(dst_path)

            parsed_url = self._get_parsed_git_url(dst_path)

            self.host = parsed_url.host
            self.url = parsed_url.url2https.replace(".git", "")
            self.repo_project_name = parsed_url.repo

            rev_parse_return_code, _ = self._run_git(
                ["rev-parse", "--verify", "--quiet", "HEAD"],
                cwd=dst_path,
                allow_error=True,
            )
            self.is_new_project = rev_parse_return_code != 0

        context["is_new_project"] = self.is_new_project
        context["host"] = self.host
        context["url"] = self.url
        context["repo_project_name"] = self.repo_project_name

        if self.is_python3_13_or_later is None and context["_copier_phase"] == "render":
            self.is_python3_13_or_later = Version(context["min_python_version"]) >= Version("3.13")

        context["is_python3_13_or_later"] = self.is_python3_13_or_later

        if ((self.given_name is None or self.family_name is None) and
            context["_copier_phase"] == "render"):
            full_name: str = context["full_name"]
            if " " in full_name:
                self.given_name, self.family_name = full_name.split(" ", 1)
            else:
                self.given_name = full_name
                self.family_name = ""

        context["given_name"] = self.given_name
        context["family_name"] = self.family_name
        return context
