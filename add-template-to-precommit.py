
#!/usr/bin/env python3
from pathlib import Path

precommit_file = Path(__file__).parent / "project_template/.pre-commit-config.yaml.jinja"

with precommit_file.open("r") as f:
    content = f.read()

    content = content.replace(
      "\n  - repo: https://github.com/astral-sh/uv-pre-commit",
      "{% if environment_manager=='uv' %}\n  - repo: https://github.com/astral-sh/uv-pre-commit"
    )

    content = content.replace(
      "    - id: uv-lock",
      "    - id: uv-lock\n{% endif -%}"
    )

with precommit_file.open("w") as f:
    f.write(content)
