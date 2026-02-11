# REIT template for Python projects


[![pipeline status](https://gitlab.ewi.tudelft.nl/reit/python-package-template/badges/main/pipeline.svg)](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/commits/main) [![Latest Release](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/badges/release.svg)](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/releases)

This template is designed to help you get started with a new Python project, or migrate an existing codebase. It includes:

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata and dependencies
- Linting + formatting via [ruff](https://docs.astral.sh/ruff/) and [prek](https://prek.j178.dev)
- [pytest](https://docs.pytest.org/en/stable/) setup and configured
- Automatic version number management with git tags via [hatch-vcs](https://github.com/ofek/hatch-vcs)
- Documentation generation via [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
- Documentation deployment, pytest and linting checks via CI/CD workflows for GitLab and Github

A course that explains in detail how to use this template is given by the REIT team.
The course materials can be accesed [here](https://reit.pages.ewi.tudelft.nl/course-python-project/outline.html).

This template is based on the [Alan Turing Institute Python project template](https://github.com/alan-turing-institute/python-project-template).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Updating your project when the template changes](#updating-your-project-when-the-template-changes)
- [Project template development](#project-template-development)
- [Advance use cases](#advance-use-cases)

## Setting up a new project

Windows users are recommended to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/).

1. Install and configure [Git](https://git-scm.com/).
Follow the instructions [here](https://docs.gitlab.com/ee/topics/git/how_to_install_git/index.html) to do so.
    * If you are on Windows and not using WSL it is recommended to disable the LF to CRLF line ending conversion `git config --global core.autocrlf false`.

3. Install [copier](https://copier.readthedocs.io/en/stable/), with the [jinja2-shell-extension](https://pypi.org/project/jinja2-shell-extension/) and with the [copier-templates-extensions](https://github.com/copier-org/copier-templates-extensions).
We recommend you install copier and the extensions with [uv](https://docs.astral.sh/uv/):

    ```bash
    uv tool install copier --with jinja2-shell-extension --with copier-templates-extensions
    ```

4. If your project will use conda, install [pixi](https://pixi.sh). Otherwise skip this step.

5. Run the following command to start the template configuration (but replace `my-package-name` with the name of your package):

    ```bash
    copier copy --trust git+https://gitlab.ewi.tudelft.nl/reit/python-package-template my-package-name
    ```

    The repository will be created in a folder called `my-package-name`.

    You will be prompted for the following information:

    - `project_name`: the name of the project.
    This will be used to name the project directory, the Python package, and the GitLab/GitHub repository.
    - `org`: the GitLab/GitHub owner of the project.
    - `host`: where to host the code: either `gitlab.tudelft`, `gitlab.ewi.tudelft` or `github`
    - `name` and `email`: the name and email of the author of the project.
    - `project_short_description`: a short description of the project.
    - `license`: the license to use for the project.
    - `min_python_version`: the lowest Python version that the project supports.
    - `environment_manager`: whether to use `uv` or `pixi` for managing the python environment.

    Great! Copier will have now created a new project in the directory you specified by replacing `my-package-name`, and customized it based on the information you provided.
    It also created a virtual environment for you and installed the project and its dependencies in it.

5. [Optional] Install ruff in your editor, for vscode see the [ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).

6. **Do the manual steps that are shown at the end of the script output.**.

7. **Have a look at the README.md file that was generated. It contains important information about the project setup and management**.

### File structure
The project has the following structure:

```
my-package-name/
├── .venv or .pixi
├── .copier-answers.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .gitlab or .github /workflows/test_code.yml
├── .gitlab or .github /workflows/deploy_docs.yml
├── LICENSE
├── README.md
├── pyproject.toml
├── mkdocs.yml
├── src/
│   └── my_package_name/
│       ├── __init__.py
│       └── main.py
├── tests/
│      └── test_my_module.py
└── docs/
       └── index.md
```

Here's a brief overview of the files and directories that have been created:

- `.venv`: The python virtual environment folder if you chose UV
- `.pixi`: The python virtual environment folder if you chose Pixi
- `.copier-answers.yml`: A file containing all your answers to copier.
- `.gitignore`: A file that tells Git which files to ignore when committing changes.
- `.pre-commit-config.yaml`: A configuration file for the `prek` tool, which runs code checks and formatting on every commit.
- `.gitlab or .github /workflows/test_code.yml`: A workflow for testing your code with a GitLab/Github action.
- `.gitlab or .github /workflows/deploy_docs.yml`: A workflow for deploying your documentation with a GitLab/Github action.
- `LICENSE`: A copy of the license you chose for your project.
- `README.md`: An overview of your project and instructions on how to manage it.
- `pyproject.toml`: A TOML file that contains metadata about your project, including its name, version, description, and dependencies.
- `mkdocs.yml`: A configuration file for `mkdocs`, which generates documentation for your code.
- `src/`: A directory that contains your Python package code.
- `tests/`: A directory that contains your tests.
- `docs/`: A directory that contains your documentation.

## Migrating an existing project

If you're taking code you've already written and want to use this template, you'll need to perform the following steps:

1. Run the copier command from the [setting up a new project](#setting-up-a-new-project) section making sure you select the folder where your project is located.
    - Do the manual steps that are shown at the end of the script output.
2. Move your library code into the `src/<project name>` directory.
    - By library code, I mean the code that you want to be importable by other Python code. If you have things like experiments, scripts, or notebooks, you should keep them in the root directory under a different name (e.g. `examples`, `notebooks` etc.)
3. Move any tests you have into the `tests` directory.
4. Go through the `pyproject.toml` file and make sure that the metadata is correct. This includes the `name`, `description`, `authors` and `license` fields.
5. Add your dependencies to the relevant section of the `pyproject.toml`.
    - If you selected `uv` as the environment manager do it like so:
        ```
        [project]
        dependencies = [
            "numpy >= 1.20,<3",
            "pandas == 1.2.3",
        ]
        ```
    - If you selected `pixi` as the environment manager do it like so:
        ```
        [tool.pixi.dependencies]
        r-base = ">=4.4.1,<5"
        ```
6. Commit your changes
7. Lint and format your whole repository
    - Run the linter and formatter with with `uv run prek run --all` or with `pixi run -e dev prek run --all-files`
    - If there are too many linting errors, add `# noqa` flags via `uvx ruff check --add-noqa` and fix them incrementally.
    - Commit your changes

## Updating your project when the template changes

Copier has [instructions on how to update a template to the latest version](https://copier.readthedocs.io/en/stable/updating/), which I'll repeat here for completeness.

If you want to update your project with the latest version of this template, you can run the following command at the root folder of your repository (ensuring that your current project is committed and that you have no uncommitted changes, since the update will overwrite some files!):

```bash
copier update --trust --skip-tasks
```

Note that this is the purpose of the `.copier-answers.yml` file in the root of your project. This file is used by Copier to keep track of the answers you gave when you first created the project, allowing it to update the project correctly when you run `copier update`.


## Project template development

If you want to make your own changes to this template:
1. Clone the repository
    ```bash
    git clone https://gitlab.ewi.tudelft.nl/reit/python-package-template.git
    ```
2. Create a virtual environment and install prek
    ```bash
    uv venv
    uv pip install prek
    uv run prek install
    ```
3. Test your local changes by generating a new project with
    ```bash
    copier copy --trust -r HEAD ./python-package-template ./my-test-project
    ```

## Advance use cases

Check out the [Netherlands eScience Center Python Template](https://github.com/NLeSC/python-template).
This includes badges, citation, github/gitlab actions for automatic code quality analysis and more.
