"""Set and use criteria to find the project root.

This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""

from pathlib import Path
from typing import Callable, Iterable, Union
from os import PathLike as _PathLike


_PathType = Union[_PathLike, str]
_CriterionType = Union[
    Callable[[_PathType], bool],
    Callable[[Path], bool],
    _PathType,
    Path,
    Iterable[Callable[[_PathType], bool]],
    Iterable[Callable[[Path], bool]],
]


def as_root_criterion(
    criterion: _CriterionType,
) -> Callable[[Path], bool]:
    if callable(criterion):
        return criterion

    # criterion must be a Collection, rather than just Iterable
    if isinstance(criterion, (_PathLike, str)):
        criterion_collection = [criterion]
    else:
        criterion_collection = list(criterion)  # type: ignore[arg-type]

    def f(path: Path) -> bool:
        for c in criterion_collection:
            if isinstance(c, (_PathLike, str)):
                if (path / c).exists():
                    return True
            else:
                if c(path):
                    return True
        return False

    return f


def has_file(file: _PathType) -> Callable[[Path], bool]:
    """
    Check that specified file exists in path.

    Note that a directory with that name will not match.
    """

    def f(path: Path) -> bool:
        return (path / file).is_file()

    return f


def has_dir(file: _PathType) -> Callable[[Path], bool]:
    """
    Check that specified directory exists.

    Note that a regular file with that name will not match.
    """

    def f(path: Path) -> bool:
        return (path / file).is_dir()

    return f


def matches_glob(pat: str) -> Callable[[Path], bool]:
    """
    Check that glob has at least one match.
    """

    def f(path: Path) -> bool:
        matches = path.glob(pat)
        try:
            # Only need to get one item from generator
            next(matches)
        except StopIteration:
            return False
        else:
            return True

    return f
