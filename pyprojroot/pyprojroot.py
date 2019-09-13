from typing import List
import pathlib as pl
import warnings


def py_project_root(path: pl.Path, project_files: List) -> pl.Path:
    """
    Recursively searches for project files in the current working directory to find
    the project root of the python project.
    :param path: pathlib path object
    :param project_files: list of to track project files
    :return: pathlib path
    """
    for file in project_files:
        found = list(path.glob(file))
        if len(found) > 0:
            return path
    return py_project_root(path.parent, project_files)


def here(project_files=(".git", "requirements.txt"), relative_project_path='.') -> pl.Path:
    """
    Returns the directory relative to the projects root directory.
    :param project_files: list of files to track inside the project
    :param relative_project_path:
    :return: pathlib path
    """
    project_path = py_project_root(pl.Path('.').cwd(), project_files)
    path = project_path.joinpath(relative_project_path)

    if path.exists():
        return path
    else:
        warnings.warn("Path doesn't exist: {}".format(path))
        return path
