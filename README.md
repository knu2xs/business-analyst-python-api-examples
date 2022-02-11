# business-analyst-python-api-examples

Examples using ArcGIS Business Analyst with Python.

## Getting Started

Read the docs - https://knu2xs.github.io/business-analyst-python-api-examples/

This is where I put all the good stuff. All of the example notebooks (and more) are all located in the `./notebooks` directory.

## Using Make - common commands

Based on the pattern provided in the [Cookiecutter Data Science template by Driven Data](https://drivendata.github.io/cookiecutter-data-science/) this template streamlines a number of commands using the `make` command pattern.

- `make env` - builds the Conda environment with name and dependencies from `environment.yml` and installs the local project package `ba_ex` using the command `python -m pip install -e ./src/src/ba_ex` so you can easily test against the package if you are working on it.

## BumpVersion Cliff Notes

[Bump2Version](https://github.com/c4urself/bump2version) is preconfigured based on hints from [this article on Medium](https://williamhayes.medium.com/versioning-using-bumpversion-4d13c914e9b8).

If you want to...

- apply a patch, `bumpversion patch`
- update version with no breaking changes (minor version update), `bumpversion minor`
- update version with breaking changes (major version update), `bumpversion major`
- create a release (tagged in vesrion control - Git), `bumpversion --tag release`

<p><small>Project based on the <a target="_blank" href="https://github.com/knu2xs/cookiecutter-geoai">cookiecutter GeoAI project template</a>. This template, in turn, is simply an extension and light modification of the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
