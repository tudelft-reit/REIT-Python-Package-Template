# {{ project_name }}

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

Install the dependencies, including the dev dependencies
    ```bash
    uv sync
    ```
or install only the runtime dependencies
    ```bash
    uv sync --no-dev
    ```
{%- elif environment_manager=='pixi' %}
Install [pixi](https://pixi.sh):

- Linux and MacOS
    ```bash
    curl -fsSL https://pixi.sh/install.sh | bash
    ```
- Windows (powershell)
    ```bash
    iwr -useb https://pixi.sh/install.ps1 | iex
    ```

Install the dependencies, including the dev dependencies
    ```bash
    pixi install --all
    ```
or install only the runtime dependencies
    ```bash
    pixi install --environment default
    ```
{% endif %}

## Usage

Execute the main script with
{% if environment_manager=='uv' %}
    ```bash
    uv run my_file.py
    ```
{%- elif environment_manager=='pixi' %}
    ```bash
    pixi run python my_file.py
    ```
{% endif %}

## Documentation

Generate the documentation locally with
{% if environment_manager=='uv' %}
    ```bash
    uv run mkdocs serve --watch ./
    ```
{%- elif environment_manager=='pixi' %}
    ```bash
    pixi run -e dev mkdocs serve --watch ./
    ```
{% endif %}

## License
{% if license=='No license' %}
Distributed under the terms of the [copyright license](LICENSE).
{% else %}
Distributed under the terms of the [{{ license }} license](LICENSE).
{% endif %}