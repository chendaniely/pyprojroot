from os import chdir
from pathlib import Path

import pytest

from pyprojroot import __version__, here


def test_version() -> None:
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "project_file",
    (".git", ".here", "my_project.Rproj", "requirements.txt", "setup.py", ".dvc"),
)
@pytest.mark.parametrize("child_dir", ("stuff", "src", "data", "data/hello"))
def test_here(tmp_path: Path, project_file: str, child_dir: str) -> None:
    """
    This test uses pytest's tmp_path facilities to create a simulated project
    directory, and checks that the path is correct.
    """
    # Create project file
    (tmp_path / project_file).write_text("blah")

    # Create child dirs
    child_path = tmp_path / child_dir
    child_path.mkdir(parents=True)
    chdir(child_path)
    assert Path.cwd() == child_path

    # Verify the project against current work directory
    assert here() == tmp_path
