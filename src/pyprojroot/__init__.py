from typing import deprecated as _deprecated

from .criterion import as_root_criterion, has_dir, has_file
from .root import find_root, find_root_with_reason


@_deprecated("Use `from pyprojroot.here import here` instead.")
def here(*args, **kwargs):
    from .here import here as h

    h(*args, **kwargs)


__all__ = [
    "as_root_criterion",
    "find_root_with_reason",
    "find_root",
    "has_dir",
    "has_file",
    "here",
]
