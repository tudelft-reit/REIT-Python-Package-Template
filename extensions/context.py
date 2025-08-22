import subprocess
from copier_templates_extensions import ContextHook
from jinja2.sandbox import SandboxedEnvironment
from pathlib import Path
from copier import __version__ as copier_version
from packaging.version import Version

class ContextUpdater(ContextHook):
    def __init__(self, environment: SandboxedEnvironment):
        super().__init__(environment)

        if Version(copier_version) < Version("9.6.0"):
            # Version 9.6 is needed for context["_copier_phase"]
            print("Update copier to version 9.6 or later")
            exit(-1)

        ret = subprocess.run(["git", "help"], capture_output=True)
        if ret.returncode != 0:
            print("Git does seem to be installed!!! Please install it and try again")
            exit(-1)

        ret = subprocess.run(["git", "config", "user.name"], capture_output=True)
        if ret.returncode != 0 or ret.stdout.decode("utf-8").strip() == "":
            print("Configure the git user.name and try again.")
            exit(-1)

        ret = subprocess.run(["git", "config", "user.email"], capture_output=True)
        if ret.returncode != 0 or ret.stdout.decode("utf-8").strip() == "":
            print("Configure the git user.email and try again.")
            exit(-1)

        self.is_new_project: bool | None = None
        self.is_python3_13_or_later: bool | None = None


    def hook(self, context: dict) -> dict:
        if self.is_new_project is None and context["_copier_phase"] == "prompt":
            dst_path = Path(context["_copier_conf"]["dst_path"]).resolve()
            self.is_new_project = not dst_path.exists()

            if self.is_new_project is False:
                ret = subprocess.run(["git", "status", "--porcelain"], capture_output=True, cwd=dst_path)
                if ret.returncode != 0:
                    print(f"Running 'git status' in '{dst_path}' failed, is this a valid git repository?")
                    exit(-1)

                if ret.stdout.decode("utf-8").strip() != "":
                    print("The repository has uncommitted changes. Please commit or stash them before proceeding.")
                    exit(-1)

        context["is_new_project"] = self.is_new_project

        if self.is_python3_13_or_later is None and context["_copier_phase"] == "render":
            self.is_python3_13_or_later = Version(context["min_python_version"]) >= Version("3.13")

        context["is_python3_13_or_later"] = self.is_python3_13_or_later
        return context
