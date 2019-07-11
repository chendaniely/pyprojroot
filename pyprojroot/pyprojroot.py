import pathlib as pl
import warnings


def pyprojroot(p, proj_files):
    for pf in proj_files:
        found = list(p.glob(pf))
        if len(found) > 0:
            return(p)
    return pyprojroot(p.parent, proj_files)


def here(rel_proj_path, proj_files=['.git', '.here', '*.Rproj']):
    proj_path = pyprojroot(pl.Path('.').cwd(), proj_files)

    pth = proj_path / rel_proj_path
    pth_str = str(pth)

    if pth.exists():
        return pth_str
    else:
        warnings.warn(f"Path doesn't exist: {pth}")
        return pth_str
