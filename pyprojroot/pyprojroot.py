import pathlib as pl
import warnings


def pyprojroot(p, proj_files):
    for pf in proj_files:
        found = list(p.glob(pf))
        if len(found) > 0:
            return(p)
    return pyprojroot(p.parent, proj_files)


def here(rel_proj_path='.',
         proj_files=['.git', '.here', '*.Rproj', '.idea', 'requirements.txt', 'setup.py']):
    proj_path = pyprojroot(pl.Path('.').cwd(), proj_files)

    pth = proj_path / rel_proj_path

    if pth.exists():
        return pth
    else:
        warnings.warn("Path doesn't exist: {}".format(pth))
        return pth
