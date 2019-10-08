# Find relative paths from a project root directory

Finding project directories in Python (data science) projects, just like there R [`here`][here] and [`rprojroot`][rprojroot] packages.

**Problem**: I have a project that has a specific folder structure,
for example, one mentioned in [Noble 2009][noble2009] or something similar to [this project template][project-template],
and I want to be able to:

1. Run my python scripts without having to specify a series of `../` to get to the `data` folder.
2. `cd` into the directory of my python script instead of calling it from the root project directory and specify all the folders to the script.
3. Reference datasets from a root directory when using a jupyter notebook because everytime I use a jupyter notebook,
  the working directory changes to the location of the notebook, not where I launched the notebook server.

**Solution**: `pyprojroot` finds the root working directory for your project as a `pathlib` object.
You can now use the `here` function to pass in a relative path from the project root directory
(no matter what working directory you are in the project),
and you will get a full path to the specified file.
That is, in a jupyter notebook,
you can write something like `pandas.read_csv(here('./data/my_data.csv'))`
instead of `pandas.read_csv('../data/my_data.csv')`.
This allows you to restructure the files in your project without having to worry about changing file paths.

Great for reading and writing datasets!

## Installation

### pip
```bash
pip install pyprojroot
```

### conda
https://anaconda.org/conda-forge/pyprojroot

```bash
conda install -c conda-forge pyprojroot 
```

## Usage

```python
from pyprojroot import here

here()
```

### Example

Load the packages
```
In [1]: from pyprojroot import here
In [2]: import pandas as pd
```

The current working directory is the "notebooks" folder
```
In [3]: !pwd
/home/dchen/git/hub/scipy-2019-pandas/notebooks
```

In the notebooks folder, I have all my notebooks
```
In [4]: !ls
01-intro.ipynb  02-tidy.ipynb  03-apply.ipynb  04-plots.ipynb  05-model.ipynb  Untitled.ipynb
```

If I wanted to access data in my notebooks I'd have to use `../data`
```
In [5]: !ls ../data
billboard.csv  country_timeseries.csv  gapminder.tsv  pew.csv  table1.csv  table2.csv  table3.csv  table4a.csv  table4b.csv  weather.csv
```

However, with there `here` function, I can access my data all from the project root.
This means if I move the notebook to another folder or subfolder I don't have to change the path to my data.
Only if I move the data to another folder would I need to change the path in my notebook (or script)
```
In [6]: pd.read_csv(here('./data/gapminder.tsv'), sep='\t').head()
Out[6]:
       country continent  year  lifeExp       pop   gdpPercap
0  Afghanistan      Asia  1952   28.801   8425333  779.445314
1  Afghanistan      Asia  1957   30.332   9240934  820.853030
2  Afghanistan      Asia  1962   31.997  10267083  853.100710
3  Afghanistan      Asia  1967   34.020  11537966  836.197138
4  Afghanistan      Asia  1972   36.088  13079460  739.981106
```

By the way, you get a `pathlib` object path back!
```
In [7]: here('./data/gapminder.tsv')
Out[7]: PosixPath('/home/dchen/git/hub/scipy-2019-pandas/data/gapminder.tsv')
```

[here]: https://github.com/r-lib/here
[rprojroot]: https://github.com/r-lib/rprojroot
[noble2009]: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424
[project-template]: https://chendaniely.github.io/sdal/2017/05/30/project_templates/
