"""
This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""

import pathlib as _pathlib
import typing
from os import PathLike as _PathLike

# TODO: It would be nice to have a class that encapsulates these checks,
# so that we can implement methods like |, !, &, ^ operators

# TODO: Refactor in a way that allows creation of reasons


def as_root_criterion(criterion) -> typing.Callable:
    if callable(criterion):
        return criterion

    # criterion must be a Collection, rather than just Iterable
    if isinstance(criterion, _PathLike):
        criterion = [criterion]
    criterion = list(criterion)

    def f(path: _pathlib.Path) -> bool:
        for c in criterion:
            if isinstance(c, _PathLike):
                if (path / c).exists():
                    return True
            else:
                if c(path):
                    return True
        return False

    return f


def has_file(file: _PathLike) -> typing.Callable:
    """
    Check that specified file exists in path.

    Note that a directory with that name will not match.
    """

    def f(path: _pathlib.Path) -> bool:
        return (path / file).is_file()

    return f


def has_dir(file: _PathLike) -> typing.Callable:
    """
    Check that specified directory exists.

    Note that a regular file with that name will not match.
    """

    def f(path: _pathlib.Path) -> bool:
        return (path / file).is_dir()

    return f


def matches_glob(pat: str) -> typing.Callable:
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
