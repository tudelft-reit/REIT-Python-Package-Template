# REIT template for Python projects


[![pipeline status](https://gitlab.ewi.tudelft.nl/reit/python-package-template/badges/main/pipeline.svg)](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/commits/main) [![Latest Release](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/badges/release.svg)](https://gitlab.ewi.tudelft.nl/reit/python-package-template/-/releases)

This template is designed to help you get started with a new Python project, or migrate an existing codebase. It includes:

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata and dependencies
- Linting + formatting via [ruff](https://docs.astral.sh/ruff/) and [prek](https://prek.j178.dev)
- [pytest](https://docs.pytest.org/en/stable/) setup and configured
- Automatic version number management with git tags via [hatch-vcs](https://github.com/ofek/hatch-vcs)
- Documentation generation via [zensical](https://zensical.org/docs)
- Documentation deployment, pytest and linting checks via CI/CD workflows for GitLab and GitHub
- A `CITATION.cff` file so others can cite your software
- VS Code settings for testing, debugging, and formatting on save

A course that explains in detail how to use this template is given by the REIT team.
The course materials can be accessed [here](https://reit.pages.ewi.tudelft.nl/course-python-project/outline.html).

This template is based on the [Alan Turing Institute Python project template](https://github.com/alan-turing-institute/python-project-template).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Updating your project when the template changes](#updating-your-project-when-the-template-changes)
- [Project template development](#project-template-development)
- [Advanced use cases](#advanced-use-cases)

## Setting up a new project

Windows users are recommended to use [WSL](https://learn.microsoft.com/en-us/windows/wsl/).

1. Install and configure [Git](https://git-scm.com/).
Follow the instructions [here](https://docs.gitlab.com/ee/topics/git/how_to_install_git/index.html) to do so.
    * If you are on Windows and not using WSL it is recommended to disable the LF to CRLF line ending conversion `git config --global core.autocrlf false`.

2. Install [copier](https://copier.readthedocs.io/en/stable/), with [jinja2-shell-extension](https://pypi.org/project/jinja2-shell-extension/), [copier-templates-extensions](https://github.com/copier-org/copier-templates-extensions) and [giturlparse](https://pypi.org/project/giturlparse/).
We recommend you install copier and the extensions with [uv](https://docs.astral.sh/uv/):

    ```bash
    uv tool install copier --with jinja2-shell-extension --with copier-templates-extensions --with giturlparse
    ```

3. If your project will use conda, install [pixi](https://pixi.sh).
Otherwise skip this step.

4. Create an empty repository on GitHub or GitLab, then clone it locally:

    ```bash
    git clone <your-empty-repo-url>
    ```

5. Run the following command from inside the cloned repository to start the template configuration:

    ```bash
    cd <your-empty-repo>
    ```

    ```bash
    copier copy --trust git+https://gitlab.ewi.tudelft.nl/reit/python-package-template .
    ```

    You will be prompted for the following information:

    - `project_name`: the name of the project.
    - `full_name` and `email`: the name and email of the author of the project.
    - `project_short_description`: a short description of the project.
    - `license`: the license to use for the project.
    - `min_python_version`: the lowest Python version that the project supports, 3.11 or higher.
    - `environment_manager`: whether to use `uv` or `pixi` for managing the python environment.
    - `manual_lint_fixes`: whether to enable linting rules that sometimes need manual fixes, or only the ones ruff always fixes automatically.

    Great! Copier will now customize the cloned repository based on the information you provided.
    It also created a virtual environment for you and installed the project and its dependencies in it.

6. [Optional] Install ruff in your editor, for vscode see the [ruff extension](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff).
VS Code will offer to install it when you open the project, and it will then fix and format your code on save.

7. **Do the manual steps that are shown at the end of the script output.**

8. **Have a look at the README.md file that was generated. It contains important information about the project setup and management**.

### File structure
The project has the following structure:

```
my-package-name/
├── .venv or .pixi
├── .copier-answers.yml
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── .gitlab-ci.yml
├── .gitlab or .github/
│   └── workflows/
│       ├── test_code.yml
│       └── deploy_docs.yml
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   └── settings.json
├── CITATION.cff
├── LICENSE
├── README.md
├── pyproject.toml
├── uv.lock or pixi.lock
├── mkdocs.yml
├── src/
│   └── my_package_name/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
└── docs/
    └── index.md
```

Here's a brief overview of the files and directories that have been created:

- `.venv`: The python virtual environment folder if you chose uv.
- `.pixi`: The python virtual environment folder if you chose pixi.
- `.copier-answers.yml`: A file containing all your answers to copier.
- `.gitignore`: A file that tells Git which files to ignore when committing changes.
- `.pre-commit-config.yaml`: A configuration file for the `prek` tool, which runs code checks and formatting on every commit.
- `.python-version`: The Python version uv uses for the virtual environment (uv only).
- `.gitlab-ci.yml`: The GitLab CI/CD entry point that includes the workflows below (GitLab only).
- `.gitlab or .github/workflows/test_code.yml`: A workflow for linting and testing your code with GitLab CI/CD or GitHub Actions.
- `.gitlab or .github/workflows/deploy_docs.yml`: A workflow for deploying your documentation with GitLab CI/CD or GitHub Actions.
- `.vscode/`: VS Code settings for running tests, debugging `main.py`, and formatting with ruff on save.
- `CITATION.cff`: Citation metadata for your software, so others know how to cite it.
- `LICENSE`: A copy of the license you chose for your project.
- `README.md`: An overview of your project and instructions on how to manage it.
- `pyproject.toml`: A TOML file that contains metadata about your project, including its name, version, description, and dependencies.
- `uv.lock` or `pixi.lock`: The exact versions of all installed dependencies.
- `mkdocs.yml`: A configuration file for `zensical`, which generates documentation for your code.
- `src/`: A directory that contains your Python package code.
- `tests/`: A directory that contains your tests.
- `docs/`: A directory that contains your documentation.

## Migrating an existing project

If you're taking code you've already written and want to use this template, you'll need to perform the following steps:

1. Commit or stash any uncommitted changes, copier will refuse to run in a repository with uncommitted changes.
2. Run the copier command from the [setting up a new project](#setting-up-a-new-project) section making sure you select the folder where your project is located.
    - Copier will ask you before overwriting any existing file.
    - It also formats your code with `ruff format` and adds `# noqa` comments for the remaining linting issues with `ruff check --add-noqa`, so that the prek checks pass.
3. Have a look at the diff of each file that was modified and add back any changes that you want to keep.
4. Move your library code into the `src/<project name>` directory.
    - By library code, I mean the code that you want to be importable by other Python code. If you have things like experiments, scripts, or notebooks, you should keep them in the root directory under a different name (e.g. `examples`, `notebooks` etc.)
5. Move any tests you have into the `tests` directory.
6. Go through the `pyproject.toml` file and make sure that the metadata is correct. This includes the `name`, `description`, `authors` and `license` fields.
7. Add your dependencies to the relevant section of the `pyproject.toml`.
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
8. Lint and format
    - With `uv run prek run --all-files` or with `pixi run -e dev prek run --all-files`
    - Fix the issues, `git add` the changes and run the linter again until all issues are gone
        - If you don't have the time to fix the issues, in the next step commit with `git commit --no-verify`
9. Commit your changes
10. If your project doesn't have version tags yet, create and push the first one:
    ```bash
    git tag v0.0.1
    git push --tags
    ```

## Updating your project when the template changes

> [!warning] Currently broken
> This is broken due to an upstream bug, see #39. In the time being, run
> `copier copy` for updates.

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
    cd python-package-template
    uv venv
    uv pip install prek
    uv run prek install
    ```
3. Test your local changes by generating a new project.
The template needs a git repository with an `origin` remote, and it can't be inside the template repository:
    ```bash
    mkdir ../my-test-project
    cd ../my-test-project
    git init
    git remote add origin https://gitlab.ewi.tudelft.nl/reit/my-test-project.git
    copier copy --trust --vcs-ref HEAD ../python-package-template .
    ```

## Advanced use cases

Check out the [Netherlands eScience Center Python Template](https://github.com/NLeSC/python-template).
This includes more badges, github/gitlab actions for automatic code quality analysis and more.
