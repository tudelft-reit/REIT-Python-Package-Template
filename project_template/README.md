# {{ project_name }}

[![Actions Status][actions-badge]][actions-link]
[![PyPI version][pypi-version]][pypi-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

{{ project_short_description }}

## Installation

{% if environment_manager=='uv' %}
Install [uv](https://docs.astral.sh/uv/):

- Linux and MacOS
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
- Windows
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Install the dependencies
    ```bash
    uv sync
    ```
or with if you do not want the dev dependencies
    ```bash
    uv sync --no-dev
    ```
{%- elif environment_manager=='pixi' %}
{% endif %}

## Usage

{% if environment_manager=='uv' %}
```bash
uv run my_file.py
```
{%- elif environment_manager=='pixi' %}
{% endif %}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for instructions on how to contribute.

## License

Distributed under the terms of the [{{ license }} license](LICENSE).


<!-- prettier-ignore-start -->
[actions-badge]:            {{url}}/workflows/CI/badge.svg
[actions-link]:             {{url}}/actions
[pypi-link]:                https://pypi.org/project/{{project_name}}/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/{{project_name}}
[pypi-version]:             https://img.shields.io/pypi/v/{{project_name}}
<!-- prettier-ignore-end -->
