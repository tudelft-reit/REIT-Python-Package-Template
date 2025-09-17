# Using GitLab EWI as a private PyPI server

The GitLab EWI server can be used as a private PyPI package repository for your Python projects.
This allows you to `pip install <your package>` in any python virtual environment while keeping your repository private.

> The steps below do not work for GitHub because it does not have a python package registry.
> Instead you can install directly from the repository:
> ```bash
> pip install git+https://<username>:<PAT>@github.com/<repo>@<tag>
> ```
> where `<tag>` is the tag of the commit or a github tag.

The original source for the steps below can be found at
- https://docs.gitlab.com/user/packages/pypi_repository/
- https://packaging.python.org/en/latest/specifications/pypirc/
- https://pip.pypa.io/en/stable/topics/configuration/#naming

## With pip, twine and build

### Install a package

#### One time setup

1. Get a `PAT` (Personal Access Token) with `api` permission [for your EWI GitLab account](https://gitlab.ewi.tudelft.nl/-/user_settings/personal_access_tokens).
2. Get the `project ID` of your repository and the `group ID` of the group the repository belongs to.
    * You can find it if you click on the three vertical dots next to the fork button for the project and next to the `New project` for the group.
3. Configure the `~/.config/pip/pip.conf` file so that `pip` knows where to install packages from.
    ```ini
    [global]
    extra-index-url = https://gitlab.ewi.tudelft.nl/api/v4/groups/<group ID>/-/packages/pypi/simple
    ```

    > `pip` is configured with group access, so it has access to every repo under that group.
    > If you need access to more than one group, you can add new groups like so.
    >
    > ```ini
    > [global]
    > extra-index-url =
    >     https://gitlab.ewi.tudelft.nl/api/v4/groups/<group ID>/-/packages/pypi/simple
    >     https://gitlab.ewi.tudelft.nl/api/v4/groups/<other group ID>/-/packages/pypi/simple
    > ```

    > `pip` can also be configured to access a single repo.
    >
    > ```ini
    > [global]
    > extra-index-url =
    >     https://gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi/simple
    > ```

4. Add the credentials to `~/.netrc` to avoid typing the `PAT` each time.
    ```ini
    machine gitlab.ewi.tudelft.nl
        login __token__
        password <PAT>
    ```
5. Restrict permissions to the file, as it contains passwords in plain text.
    ```bash
    chmod 600 .netrc
    ```
#### Install

Install the package as usual

```bash
pip install <my package>
```

### Upload a package

#### On time setup

1. Get a `PAT`, a `project ID` and a `group ID` as described in the [section above](#one-time-setup).
2. Configure the `~/.pypirc` file so that `twine` knows where to upload packages to.
    ```ini
    [distutils]
    index-servers = my-repo

    [my-repo]
    repository = https://gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi
    username = __token__
    password = <PAT>
    ```

    > `twine` is configured per repository.
    > If you want to upload wheels for a new repository, you can do add new repos like so.
    >
    > ```ini
    > [distutils]
    > index-servers =
    >     my-repo
    >     my-other-repo
    >
    > [my-repo]
    > repository = https://gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi
    > username = __token__
    > password = <PAT>
    >
    > [my-other-repo]
    > repository = https://gitlab.ewi.tudelft.nl/api/v4/projects/<other project ID>/packages/pypi
    > username = __token__
    > password = <PAT>
    > ```

5. Restrict permissions to the file, as it contain passwords in plain text.
    ```bash
    chmod 600 .pypirc
    ```
6. Install `twine` and `build`, skip this if using `uv`.
    ```bash
    pip install twine build
    ```

#### Build and upload

1. Build the wheel.
    ```bash
    python -m build
    ```
2. Upload the wheel to the package repository.
    ```bash
    twine upload -r <my-repo> dist/<my wheel>
    ```

## With `uv`

### Install a package

#### One time setup

1. Get a `PAT`, a `project ID` and a `group ID` as described in the [section above](#one-time-setup).

#### Install

There are two options:

1. From the group that the repository belongs to (preferred)
    ```bash
    uv add \
    --index-url https://<netid>:<PAT>@gitlab.ewi.tudelft.nl/api/v4/groups/<group ID>/-/packages/pypi/simple \
    <my package>
    ```

2. From the repository
    ```bash
    uv add \
    --index-url https://<netid>:<PAT>@gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi/simple \
    <my package>
    ```


### Upload a package

#### One time setup

1. Get a `PAT`, a `project ID` and a `group ID` as described in the [section above](#one-time-setup).
2. Define the index in `pyproject.toml` of your repo.
    ```toml
    [[tool.uv.index]]
    name = "gitlab"
    url = "https://gitlab.ewi.tudelft.nl/api/v4/groups/<group ID>/-/packages/pypi/simple"
    publish-url = "https://gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi"
    ```

    > If the repository is not available under the group, use the project url instead.
    > url = "https://gitlab.ewi.tudelft.nl/api/v4/projects/<project ID>/packages/pypi/simple"

#### Build and upload

1. Build the wheel.
    ```bash
    uv build
    ```
2. Export the `PAT` via env variables.
    ```bash
    export UV_PUBLISH_USERNAME=__token__
    export UV_PUBLISH_PASSWORD=<PAT>
    ```
3. Upload the wheel to the package repository.
    ```bash
    uv publish --index gitlab
    ```
