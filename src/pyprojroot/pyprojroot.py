"""DEPRECATED

This is explicitly providing the 0.2.0 version's interface of pyprojroot
and marked deprecated
"""

import warnings
from pathlib import Path
from typing import Optional, Tuple

from .criterion import _PathType, as_root_criterion
from .here import CRITERIA
from .root import find_root_with_reason


def py_project_root(path: _PathType, project_files: Tuple[str, ...]) -> Path:
    criteria = [as_root_criterion(project_file) for project_file in project_files]
    root, _ = find_root_with_reason(criteria, path)
    return root


def here(
    relative_project_path: _PathType = "",
    project_files: Optional[Tuple[str, ...]] = None,
    warn_missing: bool = False,
) -> Path:
    if project_files is None:
        path, _ = find_root_with_reason(criterion=CRITERIA, start=".")
    else:
        path = py_project_root(path=".", project_files=project_files)

    if relative_project_path:
        path = path / relative_project_path

    if warn_missing and not path.exists():
        warnings.warn(f"Path doesn't exist: {path!s}")
    return path


__all__ = ["here", "py_project_root"]

warnings.warn(
    "Importing deprecated module `pyprojroot.pyprojroot`.",
    DeprecationWarning,
)
