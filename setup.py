import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyprojroot",
    version="0.2.0",
    description="Find project root paths and return relative project files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Daniel Chen",
    author_email="chendaniely@gmail.com",
    url="https://github.com/chendaniely/pyprojroot",
    packages=setuptools.find_packages(),
    package_data={"pyprojroot": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
