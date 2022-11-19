"""
This module is inspired by the `here` library for R.
See https://github.com/r-lib/here.

It is intended for interactive use only.
"""

import pathlib as _pathlib
import warnings as _warnings
import typing

from . import criterion
from .root import find_root_with_reason


CRITERIA = [
    criterion.has_file(".here"),
    criterion.has_dir(".git"),
    criterion.matches_glob("*.Rproj"),
    criterion.has_file("requirements.txt"),
    criterion.has_file("setup.py"),
    criterion.has_dir(".dvc"),
    criterion.has_dir(".spyproject"),
    criterion.has_file("pyproject.toml"),
    criterion.has_dir(".idea"),
    criterion.has_dir(".vscode"),
]


def get_here() -> typing.Tuple[_pathlib.Path, str]:
    # TODO: This should only find_root once per session
    start = _pathlib.Path.cwd()
    path, reason = find_root_with_reason(CRITERIA, start=start)
    return path, reason


# TODO: Implement set_here


def here(
    relative_project_path: criterion._PathType = "", warn_missing: bool = False
) -> _pathlib.Path:
    """
    Returns the path relative to the projects root directory.
    :param relative_project_path: relative path from project root
    :param project_files: list of files to track inside the project
    :param warn_missing: warn user if path does not exist (default=False)
    :return: pathlib path
    """
    path, reason = get_here()
    # TODO: Show reason when requested

    if relative_project_path:
        path = path / relative_project_path

    if warn_missing and not path.exists():
        _warnings.warn(f"Path doesn't exist: {path!s}")
    return path
