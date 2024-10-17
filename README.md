# REIT template for Python projects

This template is designed to help you get started with a new Python project, or migrate an existing codebase. It includes:

- The recommended `src/` layout for a Python package
- A pre-configured `pyproject.toml` that controls your project metadata
- Linting + formatting via `ruff` and `pre-commit`
- `pytest` setup and configured
- Automatic version number management with git tags via `hatch-vcs`
- Documentation generation via `mkdocs`
- Documentation deployment and pytest checks via CI/CD workflows for Gitlab and Github
- Opt-in static type check via `mypy`

A course that explains in detail how to use this template is given by the REIT team.
The course materials can be consulted [here](https://reit.pages.ewi.tudelft.nl/course-python-best-practices/outline.html).

This template is based on the [Alan Turing Institute Python project template](https://github.com/alan-turing-institute/python-project-template).

## Sections in this README

- [Setting up a new project](#setting-up-a-new-project)
- [Migrating an existing project](#migrating-an-existing-project)
- [Updating your project when the template changes](#updating-your-project-when-the-template-changes)
- [Project template development](#project-template-development)
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
- `host`: where to host your code: either `gitlab` or `github`
- `project_short_description`: A short description of your project.
- `license`: The license to use for your project — PRs for other choices are welcome! The current supported options include:
  - `MIT`
  - `BSD-3-Clause`
  - `Apache-2.0`
  - `GPL-3.0`
- `python_name`: The name of your project when you do `import name` (and potentially `pip install name`). This should be a valid Python package name (use underscores instead of hyphens, for example).
- `typing`: Whether to use `mypy` for type checking. If you're not sure, I'd recommend basic checks (second option).
- `python_version_range`: The range of Python versions to support. This will be used to set the `python_requires` field in `pyproject.toml`. Defaults to `>=3.10`.
- `environment_manager`: whether to use `uv` or `pixi` for managing the python environment.

Great! Copier will have now created a new project in the directory you specified by replacing `my-package-name`, and customized it based on the information you provided.

Your new project will have been set up with the following structure:

```
my-package-name/
├── .copier-answers.yml
├── .gitignore
├── .pre-commit-config.yaml
├── <.gitlab/github>/workflows/test_code.yml
├── <.gitlab/github>/workflows/deploy_docs.yml
├── CODE_OF_CONDUCT.md
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

- `.copier-answers.yml`: A file containing all your answers to copier.
- `.gitignore`: A file that tells Git which files to ignore when committing changes.
- `.pre-commit-config.yaml`: A configuration file for the `pre-commit` tool, which runs code checks and formatting on every commit.
- `<.gitlab/github>/workflows/test_code.yml`: A workflow for testing your code in a Github/Gitlab workflow.
- `<.gitlab/github>/workflows/deploy_docs.yml`: A workflow for deploying your documentation in a Github/Gitlab workflow.
- `CODE_OF_CONDUCT.md`: A code of conduct for your project, which sets out the standards of behaviour you expect from contributors. You will likely need to edit or extend this to suit your project.
- `LICENSE`: A copy of the license you chose for your project.
- `README.md`: An overview of your project and instructions on how to manage it.
- `pyproject.toml`: A TOML file that contains metadata about your project, including its name, version, description, and dependencies.
- `mkdocs.yml`: A configuration file for `mkdocs`, which generates documentation for your code.
- `src/`: A directory that contains your Python package code.
- `tests/`: A directory that contains your tests.
- `docs/`: A directory that contains your tests.

**Have a look at the README.md file that was generated. It contains important information about the project setup and management**

### Migrating an existing project

If you're taking code you've already written and want to use this template, you'll need to perform the following steps:

- Make sure there are no untracked changes in your repository
- Run the copier command from the [setting up a new project](#setting-up-a-new-project) section making sure you select the folder where your project is located.
  - **Do not run any of the commands that are shown the end**
- If you were not using pixi or uv, install and setup according to the instructions shown in the previous step
- Move your library code into the `src/{{ python_name }}` directory.
  - By library code, I mean the code that you want to be importable by other Python code. If you have things like experiments, scripts, or notebooks, you should keep them in the root directory under a different name (e.g. `examples`, `notebooks` etc.)
- Move any tests you have into the `tests` directory.
- Go through the `pyproject.toml` file and make sure that the metadata is correct. This includes the `name`, `description`, `version`, `authors`, `license`, and `classifiers` fields.
- Add your dependencies to the relevant section of the `pyproject.toml` file under the `install_requires` field. Dependencies are formatted like this:
    ```
    [project]
    dependencies = [
        "numpy >= 1.20,<3",
        "pandas == 1.2.3",
    ]
    ```
    where the first part is the package name, and the second part is the version specifier. You can find more information on version specifiers [here](https://www.python.org/dev/peps/pep-0440/#version-specifiers) to help you write these.
- If you have conda dependencies, place them under the pixi section
    ```
    [tool.pixi.dependencies]
    r-base = ">=4.4.1,<5"
    ```
- Commit your changes
- Lint and format your whole repository 
  - Install `pre-commit` via uv or pixi
  - Format with `pre-commit run --all`
  - If there are too many linting errors, add `# noqa` flags via `uvx ruff check --add-noqa` and fix them incrementally

**Have a look at the README.md file that was generated. It contains important information about the project setup and management**

## Updating your project when the template changes

Copier has [instructions on how to update a template to the latest version](https://copier.readthedocs.io/en/stable/updating/), which I'll repeat here for completeness.

If you want to update your project with the latest version of this template, you can run the following command at the root folder of your repository (ensuring that your current project is committed and that you have no uncommitted changes, since the update will overwrite some files!):

```bash
uvx copier update
```

Note that this is the purpose of the `.copier-answers.yml` file in the root of your project. This file is used by Copier to keep track of the answers you gave when you first created the project, allowing it to update the project correctly when you run `copier update`.


## Project template development

If you want to make your own changes to this template, clone the repository
```bash
git clone https://gitlab.ewi.tudelft.nl/reit/python-package-template.git
```
and test your local changes by generating a new project with
```bash
uvx copier copy -r HEAD ./python-project-template ./my-test-project
```

## Inspiration

For more advance use cases, check out the [Netherlands eScience Center Python Template](https://github.com/NLeSC/python-template).
This includes badges, citation, github/gitlab actions for automatic code quality analysis and more.
