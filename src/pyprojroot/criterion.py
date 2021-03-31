"""
This module is inspired by the `rprojroot` library for R.
See https://github.com/r-lib/rprojroot.

It is intended for interactive or programmatic only.
"""

__all__ = [
    "CriterionFunction",
    "Criterion",
    "Criteria",
    "as_root_criterion",
    "has_file",
    "has_dir",
    "matches_glob",
]

# TODO: It would be nice to have a class that encapsulates these checks,
# so that we can implement methods like |, !, &, ^ operators

# TODO: Refactor in a way that allows creation of reasons


from pathlib import Path
from typing import Union, Iterable, AnyStr
from typing_extensions import Protocol, runtime_checkable

from os import PathLike


@runtime_checkable
class CriterionFunction(Protocol):
    def __call__(self, path: Path) -> bool:
        ...


Criterion = Union[CriterionFunction, "PathLike[AnyStr]"]


Criteria = Iterable[Criterion]


def as_root_criterion(criterion: Union[Criterion, Criteria]) -> CriterionFunction:
    if isinstance(criterion, CriterionFunction):
        return criterion

    # criterion must be a Collection, rather than just Iterable
    criteria: Criteria
    if isinstance(criterion, PathLike):
        criteria = [criterion]
    else:
        criteria = list(criterion)

    def f(path: Path) -> bool:
        for c in criteria:
            if isinstance(c, PathLike):
                if (path / c).exists():
                    return True
            else:
                if c(path):
                    return True
        return False

    return f


def has_file(file: Union[str, "PathLike[str]"]) -> CriterionFunction:
    """
    Check that specified file exists in path.

    Note that a directory with that name will not match.
    """

    def f(path: Path) -> bool:
        return (path / file).is_file()

    return f


def has_dir(file: Union[str, "PathLike[str]"]) -> CriterionFunction:
    """
    Check that specified directory exists.

    Note that a regular file with that name will not match.
    """

    def f(path: Path) -> bool:
        return (path / file).is_dir()

    return f


def matches_glob(pat: str) -> CriterionFunction:
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
