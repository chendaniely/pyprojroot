"""
This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""
__all__ = ["as_start_path", "find_root_with_reason", "find_root"]

from os import PathLike
from pathlib import Path
from typing import Tuple, Optional, Union

from .criterion import as_root_criterion, Criterion, CriterionFunction


def as_start_path(start: Optional[Union["PathLike[str]"]]) -> Path:
    if start is None:
        return Path.cwd()
    if not isinstance(start, Path):
        start = Path(start)
    # TODO: consider `start = start.resolve()`
    return start


def find_root_with_reason(
    criterion: Criterion, start: Optional["PathLike[str]"] = None
) -> Tuple[Path, str]:
    """
    Find directory matching root criterion with reason.

    Recursively search parents of start path for directory
    matching root criterion with reason.
    """
    # TODO: Implement reasons

    # Prepare inputs
    root_criterion: CriterionFunction = as_root_criterion(criterion)
    start_path: Path = as_start_path(start)

    # Check start
    if start_path.is_dir() and root_criterion(start_path):
        return start_path, "Pass"

    # Iterate over all parents
    # TODO: Consider adding maximum depth
    # TODO: Consider limiting depth to path (e.g. "if p == stop: raise")
    for p in start_path.parents:
        if root_criterion(p):
            return p, "Pass"

    # Not found
    raise RuntimeError("Project root not found.")


def find_root(criterion: Criterion, start: Optional["PathLike[str]"] = None) -> Path:
    """
    Find directory matching root criterion.

    Recursively search parents of start path for directory
    matching root criterion.
    """
    try:
        root, _ = find_root_with_reason(criterion, start)
    except RuntimeError as ex:
        raise ex
    else:
        return root
