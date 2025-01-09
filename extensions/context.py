import subprocess
from copier_templates_extensions import ContextHook

class ContextUpdater(ContextHook):
    def __init__(extension_self, environment):
        super().__init__(environment)

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


    def hook(self, context):
        return context
