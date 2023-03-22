import os

import pytest

from src.pyprojroot.root import as_start_path, find_root

MARKER = ".here"


@pytest.fixture
def temp_dir_structure(tmp_path):
    """
    Create a pytest temp path for testing:

    tmp_path/
    └── dir1/
        ├── .here  <-- marker file
        └── dir2/
    """
    dir1 = tmp_path / "dir1"
    dir2 = dir1 / "dir2"
    os.makedirs(dir1 / MARKER)
    os.makedirs(dir2)
    return dir1, dir2


def test_as_start_path_normalized_path():
    result01 = as_start_path("~")  # Home
    assert result01.is_dir()

    result02 = as_start_path("~/.")  # Still at Home
    assert result02.is_dir()
    assert result01 == result02

    result03 = as_start_path("~/..")  # One directory below Home
    assert result03.is_dir()
    assert result03 != result02


def test_find_root_marker_in_child(temp_dir_structure):
    """Marker is in child folder, checking the parent should raise."""
    dir1, _ = temp_dir_structure

    os.chdir(dir1)
    result = find_root(MARKER, start=".")
    assert result.is_dir()

    with pytest.raises(RuntimeError, match="Project root not found."):
        find_root(MARKER, start="..")


def test_find_root_marker_in_parent(temp_dir_structure):
    """Marker in parent - child and parent should successfully find a root."""
    _, dir2 = temp_dir_structure
    os.chdir(dir2)
    result01 = find_root(MARKER, start=".")
    assert result01.is_dir()

    result02 = find_root(MARKER, start="..")
    assert result02.is_dir()
