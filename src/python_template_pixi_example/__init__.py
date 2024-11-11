"""
python-template-pixi-example: A python template pixi example.
"""

from __future__ import annotations

import json
import sys
from importlib.metadata import Distribution, version


def _is_editable() -> bool:
    dist = Distribution.from_name("python-template-pixi-example")

    if sys.version_info >= (3, 13):
        editable = dist.origin.dir_info.editable
    else:
        direct_url = dist.read_text("direct_url.json")
        if direct_url is None:
            return False

        editable = json.loads(direct_url).get("dir_info", {}).get("editable", False)

    if not isinstance(editable, bool):
        return False

    return editable


if _is_editable():
    # Development way of getting the version, it is dynamically updated on each call
    try:
        # setuptools_scm is not included in the runtime virtual environment
        # importing it raises an ImportError,
        # it also fails in the gitlab CI with a UserWarning error
        from setuptools_scm import get_version

        # This will fail with LookupError if Git is not installed
        __version__ = get_version(root="../..", relative_to=__file__)
    except (ImportError, LookupError, UserWarning):
        __version__ = version(__name__)
else:
    # Get the version as specified by the wheel
    __version__ = version(__name__)

__all__ = ("__version__",)
