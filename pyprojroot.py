import pathlib as pl
import warnings

PROJ_FILES = ['.git', '.here', '*.Rproj']

def pyprojroot(p):
    try:
        for pf in PROJ_FILES:
            found = list(p.glob(pf))
            if len(found) > 0:
                return(p)
        return pyprojroot(p.parent)
    except RecursionError:
        print(f'Unable to find pyprojroot path, returning {p.cwd()}')
        return p.cwd()

def here(rel_proj_path):
    proj_path = pyprojroot(pl.Path('.').cwd())
    print('here')
    p = proj_path / rel_proj_path
    s = str(p)

    if p.exists():
        return s
    else:
        warnings.warn(f"Path doesn't exist: {p}")
        return s

print(here('./data/gapminder.tsv'))

import pandas as pd
pd.read_csv(here('./data/gapminder.tsv'), sep='\t').head()
