# Template for Python projects

This template is designed to help you get started with a new Python project, or migrate an existing codebase. It includes:

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata
- Linting + formatting via `ruff` and `pre-commit`
- `pytest` set up to run automatically on your commits through pre-commit
- Version updates via git tags
- Opt-in typing support via `mypy`

Based on the [Alan Turing Institute Python project template](https://github.com/alan-turing-institute/python-project-template).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Using your new project](#using-your-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Python environment management](#python-environment-management)
- [Installing your package in editable mode](#installing-your-package-in-editable-mode)
- [Wrtiting code and running tests](#writing-code-and-running-tests)
- [Formatting and checking your code](#formatting-and-checking-your-code)
- [Publishing your package](#publishing-your-package)
- [Updating your project when the template changes](#updating-your-project-when-the-template-changes)
- [Inspiration](#inspiration)

## Setting up a new project

To use, install [uv](https://docs.astral.sh/uv/):

- Linux and MacOS
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
- Windows
    ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

Then, run the following command to start the template configuration (but replace `my-package-name` with the name of your package):

```
uvx copier copy git+https://gitlab.ewi.tudelft.nl/reit/python-package-template my-package-name
```

The output will be created in a folder called `my-package-name`, and will be created if it doesn't exist.

You will be prompted for the following information:

- `project_name`: The name of your project. This will be used to name the
  project directory, the Python package, and the GitHub repository.
- `project_short_description`: A short description of your project.
- `license`: The license to use for your project — PRs for other choices are welcome! The current supported options include:
  - `MIT`
  - `BSD-3-Clause`
  - `Apache-2.0`
  - `GPL-3.0`
- `python_name`: The name of your project when you do `import name` (and potentially `pip install name`). This should be a valid Python package name (use underscores instead of hyphens, for example).
- `typing`: Whether to use `mypy` for type checking. If you're not sure, I'd recommend basic checks (second option).
- `python_version_range`: The range of Python versions to support. This will be used to set the `python_requires` field in `pyproject.toml`. Defaults to `>=3.10`.

Great! Copier will have now created a new project in the directory you specified by replacing `my-package-name`, and customized it based on the information you provided.

Your new project will have been set up with the following structure:

```
my-package-name/
├── .gitignore
├── .pre-commit-config.yaml
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── README.md
├── pyproject.toml
├── src/
│   └── my_package_name/
│       └── __init__.py
└── tests/
    └── __init__.py
```

Here's a brief overview of the files and directories that have been created:

- `.gitignore`: A file that tells Git which files to ignore when committing changes.
- `.pre-commit-config.yaml`: A configuration file for the `pre-commit` tool, which runs code checks and formatting on every commit.
- `CONTRIBUTING.md`: A guide for people who want to contribute to your project, which has a lot of the same advice as this README.
- `CODE_OF_CONDUCT.md`: A code of conduct for your project, which sets out the standards of behaviour you expect from contributors. You will likely need to edit or extend this to suit your project.
- `LICENSE`: A copy of the license you chose for your project.
- `README.md`: An overview of your project, which comes with some badges (example: ![Badge](https://img.shields.io/badge/this_is-a_badge-blue)) for things like CI status, code coverage, and PyPI version.
- `pyproject.toml`: A TOML file that contains metadata about your project, including its name, version, description, and dependencies.
- `src/`: A directory that contains your Python package code.
- `tests/`: A directory that contains your tests.

### Migrating an existing project

If you're taking code you've already written and want to use this template, you'll need to perform the following steps:

- Start by moving your library code into the `src/{{ python_name }}` directory.
  - By library code, I mean the code that you want to be importable by other Python code. If you have things like experiments, scripts, or notebooks, you should keep them in the root directory under a different name (e.g. `examples`, `notebooks` etc.)
- Copy over any tests you have into the `tests` directory.
- Go through the `pyproject.toml` file and make sure that the metadata is correct. This includes the `name`, `description`, `version`, `authors`, `license`, and `classifiers` fields.
- Add your dependencies to the relevant section of the `pyproject.toml` file under the `install_requires` field. Dependencies are formatted like this:
    ```
    [project]
    install_requires = [
        "numpy >= 1.20",
        "pandas == 1.2.3",
        "scipy",
    ]
    ```
    where the first part is the package name, and the second part is the version specifier. You can find more information on version specifiers [here](https://www.python.org/dev/peps/pep-0440/#version-specifiers) to help you write these.

Once you've set up your new project, you can start developing your package. There are some guidelines for development included in the [`CONTRIBUTING.md`](project_template/CONTRIBUTING.md) file generated in your project, but the main things are repeated below.


## Python environment management

Every project should have a Python environment set up to manage dependencies.
We recommend using [`uv`](https://astral.sh/uv) or [`pixi`](https://pixi.sh/).
Instructions for setting up both are shown when the template setup is finished.

## Writing code and running tests

You're now ready to start developing your package! Add code to the `src` directory, tests to the `tests` directory, and run your tests with the  `pytest` command to make sure everything is working as expected. Settings for `pytest` are included in the `pyproject.toml` file.

Additionally, the automated CI pipeline will run the tests for you, but it's a good idea to run them locally as well to catch any issues before you push your code.

## Formatting and checking your code

The tools for formatting and linting your code for errors are all bundled with [pre-commit](https://pre-commit.com/). Included are:
- [ruff](https://astral.sh/ruff) (linting + formatting)
- [mypy](https://mypy.readthedocs.io/en/stable/) (static type checking)
- various other small fixes and checks (see the [`.pre-commit-config.yaml`](project_template/.pre-commit-config.yaml) file for more information)

To have pre-commit check your files before you commit them, you can run the following command:

```bash
pre-commit install
```

This will set up pre-commit to run the checks automatically on your files before you commit them. It's possible that pre-commit will make changes to your files when it runs the checks, so you should add those changes to your commit before you commit your code. A typical workflow would look like this:

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
pre-commit run --all-files
```

This will run the checks on all files in your git project, regardless of whether they're staged for commit or not.

## Publishing your package

If you're ready to publish your package to [PyPI](https://pypi.org/) (i.e. you want to be able to run `pip install my-package-name` from anywhere), follow the [uv instructions](https://docs.astral.sh/uv/guides/publish/).
In short, they boil down to running `uv build` and `uv publish`.

## Updating your project when the template changes

Copier has [instructions on how to update a template to the latest version](https://copier.readthedocs.io/en/stable/updating/), which I'll repeat here for completeness.

If you want to update your project with the latest version of this template, you can run the following command (ensuring that your current project is committed and that you have no uncommitted changes, since the update will overwrite some files!):

```bash
copier update
```

Note that this is the purpose of the `.copier-answers.yml` file in the root of your project. This file is used by Copier to keep track of the answers you gave when you first created the project, allowing it to update the project correctly when you run `copier update`.


## Inspiration

This template heavily draws upon the [Alan Turing Institute Python project template](https://github.com/alan-turing-institute/python-project-template).
For more advance use cases, check out the [Netherlands eScience Center Python Template](https://github.com/NLeSC/python-template).
This includes badges, citation, github/gitlab actions, automatic code quality and more.
