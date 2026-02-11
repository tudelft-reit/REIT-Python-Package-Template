
#!/usr/bin/env python3
from pathlib import Path

template_file = Path(__file__).parent / "project_template/.pre-commit-config.yaml.jinja"
rendered_file = Path(__file__).parent / "project_template/.pre-commit-config.yaml"
temp_template_file = Path(__file__).parent / "project_template/.tmp-pre-commit-config.yaml.jinja"

version_key = "rev:"

updated_versions = []
with rendered_file.open() as f:
    for line in f:
        if version_key in line:
            updated_versions.append(line.split(version_key)[-1])

with template_file.open() as f, temp_template_file.open("w") as temp_f:
    for line in f:
        out_line = line
        if version_key in line:
            out_line = line.split(version_key)[0] + version_key + updated_versions.pop(0)
        temp_f.write(out_line)

temp_template_file.rename(template_file)
