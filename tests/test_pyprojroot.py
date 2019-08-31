from pyprojroot import __version__, here
import os
import pytest
from pathlib import Path


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize(
    "proj_file",
    [
        ".git",
        ".here",
        "my_project.Rproj",
        "requirements.txt",
        "setup.py",
        ".dvc",
    ],
)
@pytest.mark.parametrize("child_dir", ["stuff", "src", "data", "data/hello"])
def test_here(tmpdir, proj_file, child_dir):
    """
    This test uses pytest's tmpdir facilities to create a simulated project
    directory, and checks that the path is correct.
    """
    # Make proj_file
    tmpdir = Path(tmpdir)
    p = tmpdir / proj_file
    with p.open("w") as fpath:
        fpath.write("blah")

    # Make child dirs
    (tmpdir / child_dir).mkdir(parents=True)
    os.chdir(tmpdir / child_dir)
    assert os.getcwd() == str(tmpdir / child_dir)

    # Check that proj
    path = here()
    assert path == tmpdir
