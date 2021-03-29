"""
This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""

import pathlib as _pathlib
import typing as _typing
from os import PathLike as _PathLike

from .criterion import as_root_criterion as _as_root_criterion


def as_start_path(start: _PathLike) -> _pathlib.Path:
    if start is None:
        return _pathlib.Path.cwd()
    if not isinstance(start, _pathlib.Path):
        start = _pathlib.Path(start)
    # TODO: consider `start = start.resolve()`
    return start


def find_root_with_reason(
    criterion, start: _PathLike = None
) -> _typing.Tuple[_pathlib.Path, str]:
    """
    Find directory matching root criterion with reason.

    Recursively search parents of start path for directory
    matching root criterion with reason.
    """
    # TODO: Implement reasons

    # Prepare inputs
    criterion = _as_root_criterion(criterion)
    start = as_start_path(start)

    # Check start
    if start.is_dir() and criterion(start):
        return start, "Pass"

    # Iterate over all parents
    # TODO: Consider adding maximum depth
    # TODO: Consider limiting depth to path (e.g. "if p == stop: raise")
    for p in start.parents:
        if criterion(p):
            return p, "Pass"

    # Not found
    raise RuntimeError("Project root not found.")


def find_root(criterion, start: _PathLike = None, **kwargs) -> _pathlib.Path:
    """
    Find directory matching root criterion.

    Recursively search parents of start path for directory
    matching root criterion.
    """
    try:
        root, _ = find_root_with_reason(criterion, start=start, **kwargs)
    except RuntimeError as ex:
        raise ex
    else:
        return root
