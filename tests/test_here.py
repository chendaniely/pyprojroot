import os

import pytest

from src.pyprojroot.here import here


@pytest.mark.parametrize(
    "project_files,file_type",
    [
        (".git", "dir"),
        (".here", "file"),
        ("my_project.Rproj", "file"),
        ("requirements.txt", "file"),
        ("setup.py", "file"),
        (".dvc", "dir"),
    ],
)
@pytest.mark.parametrize("child_dir", ["stuff", "src", "data", "data/hello"])
def test_here(tmp_path, project_files, file_type, child_dir):
    """
    This test uses pytest's tmp_path facilities to create a simulated project
    directory, and checks that the path is correct.
    """
    # Create project file
    if file_type == "file":
        (tmp_path / project_files).write_text("blah")
    elif file_type == "dir":
        (tmp_path / project_files).mkdir(parents=True)
    else:
        raise ValueError("Invalid input: {file_type}")

    # Create child dirs
    start_dir = tmp_path / child_dir
    start_dir.mkdir(parents=True)
    os.chdir(start_dir)

    # Verify the project against current work directory
    current_path = here()
    assert current_path == tmp_path
