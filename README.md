# python-template-pixi-example

A python template pixi example.

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


1. Install [pixi](https://pixi.sh):

    - Linux and MacOS

        ```bash
        curl -fsSL https://pixi.sh/install.sh | bash
        ```
    - Windows (powershell)

        ```bash
        iwr -useb https://pixi.sh/install.ps1 | iex
        ```

2. Install the dependencies, including the dev dependencies

    ```bash
    pixi install --all
    ```
    or install only the runtime dependencies

    ```bash
    pixi install --environment default
    ```


3. Install the pre-commit hook.
This will set up pre-commit to run the checks automatically on your files before you commit them.

    ```bash
    pixi run -e dev pre-commit install
    ```


## Running the main script

Execute the main script with

```bash
pixi run main_script
```


## Adding dependencies


### Pypi packages
Add dependencies by running
```bash
pixi add --pypi numpy
```
if you want to install torch with CUDA support, add the following line to the `pyproject.toml` under `[tool.pixi.project]`
```toml
pypi-options = { extra-index-urls = ["https://download.pytorch.org/whl/cu121"] }
```
then run
```bash
pixi add --pypi torch==2.4.1+cu121 torchaudio==2.4.1+cu121 torchvision==0.19.1+cu121
```

### Conda packages
Add dependencies by running
```bash
pixi add numpy
```
to install pytorch with cuda support as a conda package add the additional channels to the `pyproject.toml`:
```toml
[tool.pixi.project]
channels = ["nvidia", "conda-forge", "pytorch"]
```
and the add the dependencies manually with channel restrictions like so:
 ```toml
[tool.pixi.dependencies]
pytorch = {version=">=2.5.1,<3", channel="pytorch"}
torchvision = {version=">=0.20.1,<1", channel="pytorch"}
torchaudio = {version=">=2.5.1,<3", channel="pytorch"}
pytorch-cuda = "12.4.*"
```
the run `pixi install` to download and install pytorch on the environment.
For more information check out the [pixi channel logic section](https://pixi.sh/latest/advanced/channel_priority/#use-case-pytorch-and-nvidia-with-conda-forge).


## Running tests

Run your tests with

```bash
pixi run -e dev pytest --cov=src ./tests
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
pixi run -e dev pre-commit run --all-files
```


This will run the checks on all files in your git project, regardless of whether they're staged for commit or not.

## Documentation

Generate the documentation locally with

```bash
pixi run -e dev mkdocs serve --watch ./
```


## Versions

Versions are managed automatically via [hatch-vcs](https://github.com/ofek/hatch-vcs), which follows the versioning scheme from [setuptools-scm](https://setuptools-scm.readthedocs.io/en/latest/usage/#default-versioning-scheme).

To create a new version, tag the code with `git tag <version>`, e.g. `git tag v0.1.0`, and push the tag with `git push --tags`.

You can check the version by running

```bash
pixi run -e dev hatch version
```


In python you can see the version with
```python
from python_template_pixi_example import __version__

print(f"python_template_pixi_example version is { __version__ }")
```

## Publishing the package

Pixi does not support yet building and publishing conda packages.
In the meantime, you can build and publish your package using [rattler-build](https://github.com/prefix-dev/rattler-build/) or [conda-build](https://docs.conda.io/projects/conda-build/en/latest/).


## License

Distributed under the terms of the [GPL license](LICENSE).
