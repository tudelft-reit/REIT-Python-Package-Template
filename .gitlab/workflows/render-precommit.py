#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('.pre-commit-config.yaml.jinja')

context = {'environment_manager': 'uv'}

output = template.render(context)

with open('.pre-commit-config.yaml', 'w') as f:
    f.write(output)
