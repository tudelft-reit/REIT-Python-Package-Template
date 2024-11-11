# python-template-uv-example

A python template uv example.

## Sections in this README

- [Installation](#installation)
- [Running the main script](#running-the-main-script)
- [Adding dependencies](#adding-dependencies)
- [Running test](#running-tests)
- [Formatting and checking](#formatting-and-checking)
- [Documentation](#documentation)
- [Versions](#versions)
- [Publishing your package](#publishing-the-package)
- [License](#license)

## Installation


1. Install [uv](https://docs.astral.sh/uv/):

    - Linux and MacOS

        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```
    - Windows

        ```bash
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```

2. Install the dependencies, including the dev dependencies

    ```bash
    uv sync
    ```
    or install only the runtime dependencies

    ```bash
    uv sync --no-dev
    ```

3. Install the pre-commit hook.
This will set up pre-commit to run the checks automatically on your files before you commit them.

    ```bash
    uv run pre-commit install
    ```

## Running the main script

Execute the main script with

```bash
uv run main_script
```

## Adding dependencies


Add dependencies by running
```bash
uv add numpy
```
if you want to install torch with CUDA support, you can do it via:
```bash
uv add torch==2.4.1+cu121 torchaudio==2.4.1+cu121 torchvision==0.19.1+cu121 --extra-index-url https://download.pytorch.org/whl/cu121
```

## Running tests

Run your tests with

```bash
uv run pytest --cov=src ./tests
```

## Formatting and checking

The tools for formatting and linting your code for errors are all bundled with [pre-commit](https://pre-commit.com/). Included are:
- [ruff](https://astral.sh/ruff) - linting and formatting
- [yamlfix](https://github.com/lyz-code/yamlfix) - linting and formatting for .yaml files
- various other small fixes and checks (see the [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file for more information)

It's possible that pre-commit will make changes to your files when it runs the checks, so you should add those changes to your commit before you commit your code. A typical workflow would look like this:

```bash
git add -u
git commit -m "My commit message"
# pre-commit will run the checks here; if it makes changes, you'll need to add them to your commit
git add -u
git commit -m "My commit message"
# changes should have all been made by now and the commit should pass if there are no other issues
# if your commit fails again here, you have to fix the issues manually (not everything can be fixed automatically).
```

One thing that is worth knowing is how to lint your files outside of the context of a commit. You can run the checks manually by running the following command:

```bash
uv run pre-commit run --all-files
```

This will run the checks on all files in your git project, regardless of whether they're staged for commit or not.

## Documentation

Generate the documentation locally with

```bash
uv run mkdocs serve --watch ./
```

## Versions

Versions are managed automatically via [hatch-vcs](https://github.com/ofek/hatch-vcs), which follows the versioning scheme from [setuptools-scm](https://setuptools-scm.readthedocs.io/en/latest/usage/#default-versioning-scheme).

To create a new version, tag the code with `git tag <version>`, e.g. `git tag v0.1.0`, and push the tag with `git push --tags`.

You can check the version by running

```bash
uv run hatch version
```

In python you can see the version with
```python
from python_template_uv_example import __version__

print(f"python_template_uv_example version is { __version__ }")
```

## Publishing the package


If you're ready to publish your package to [PyPI](https://pypi.org/) (i.e. you want to be able to run `pip install my-package-name` from anywhere), follow the [uv instructions](https://docs.astral.sh/uv/guides/publish/).
In short, they boil down to running:

1. Build the wheel

    ```bash
    uv build
    ```

2. Upload the wheel to PyPI

    ```bash
    uv publish
    ```

## License

Distributed under the terms of the [GPL license](LICENSE).
