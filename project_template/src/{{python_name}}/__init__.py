"""
{{ project_name }}: {{ project_short_description }}
"""

from __future__ import annotations

try:
    # Development way of getting the version, always correct, it is dynamically updated

    # setuptools_scm might not included in the runtime dependencies, raising ImportError
    # it also fails on the gitlab CI with a UserWarning error
    from setuptools_scm import get_version

    # This will fail with LookupError if the package is not installed in editable mode
    # or if Git is not installed
    __version__ = get_version(root="../..", relative_to=__file__)
except (ImportError, LookupError, UserWarning):
    # Standard way of getting the version, pulls it from the _version.py file
    from importlib.metadata import version

    __version__ = version(__name__)

__all__ = ("__version__",)
