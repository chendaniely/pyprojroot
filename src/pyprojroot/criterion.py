"""
This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""

import pathlib as _pathlib
import typing
from os import PathLike as _PathLike


_PathType = typing.Union[_PathLike, str]
_CriterionType = typing.Union[
    typing.Callable[[_PathType], bool],
    typing.Callable[[_pathlib.Path], bool],
    _PathType,
    _pathlib.Path,
    typing.Iterable[typing.Callable[[_PathType], bool]],
    typing.Iterable[typing.Callable[[_pathlib.Path], bool]],
]

# TODO: It would be nice to have a class that encapsulates these checks,
# so that we can implement methods like |, !, &, ^ operators

# TODO: Refactor in a way that allows creation of reasons


def as_root_criterion(
    criterion: _CriterionType,
) -> typing.Callable[[_pathlib.Path], bool]:
    if callable(criterion):
        return criterion

    # criterion must be a Collection, rather than just Iterable
    if isinstance(criterion, _PathLike):
        criterion_collection = [criterion]
    else:
        criterion_collection = list(criterion)  # type: ignore[arg-type]

    def f(path: _pathlib.Path) -> bool:
        for c in criterion_collection:
            if isinstance(c, _PathLike):
                if (path / c).exists():
                    return True
            if callable(c):
                if c(path):
                    return True
        return False

    return f


def has_file(file: _PathType) -> typing.Callable[[_pathlib.Path], bool]:
    """
    Check that specified file exists in path.

    Note that a directory with that name will not match.
    """

    def f(path: _pathlib.Path) -> bool:
        return (path / file).is_file()

    return f


def has_dir(file: _PathType) -> typing.Callable[[_pathlib.Path], bool]:
    """
    Check that specified directory exists.

    Note that a regular file with that name will not match.
    """

    def f(path: _pathlib.Path) -> bool:
        return (path / file).is_dir()

    return f


def matches_glob(pat: str) -> typing.Callable[[_pathlib.Path], bool]:
    """
    Check that glob has at least one match.
    """

    def f(path: _pathlib.Path) -> bool:
        matches = path.glob(pat)
        try:
            # Only need to get one item from generator
            next(matches)
        except StopIteration:
            return False
        else:
            return True

    return f
