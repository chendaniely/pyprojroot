from os import chdir
from pathlib import Path

import pytest

from pyprojroot import __version__, here


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "project_files",
    (".git", ".here", "my_project.Rproj", "requirements.txt", "setup.py", ".dvc"),
)
@pytest.mark.parametrize("child_dir", ["stuff", "src", "data", "data/hello"])
def test_here(tmpdir, project_files, child_dir):
    """
    This test uses pytest's tmpdir facilities to create a simulated project
    directory, and checks that the path is correct.
    """
    # Create project file
    temp_dir = Path(tmpdir)
    path = temp_dir / project_files
    with path.open("w") as file_path:
        file_path.write("blah")

    # Create child dirs
    (temp_dir / child_dir).mkdir(parents=True)
    chdir(temp_dir / child_dir)
    assert Path().cwd() == (temp_dir / child_dir)

    # Verify the project against current work directory
    current_path = here()
    assert current_path == temp_dir
