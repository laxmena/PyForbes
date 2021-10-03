# PyForbes - Python wrapper for Forbes API

<a href="https://codeclimate.com/github/laxmena/PyForbes/maintainability"><img src="https://api.codeclimate.com/v1/badges/12cadf4283a14dbb59eb/maintainability" /></a> [![CircleCI](https://circleci.com/gh/laxmena/PyForbes/tree/main.svg?style=svg)](https://circleci.com/gh/laxmena/PyForbes/tree/main) [![PyPI Python Version](https://img.shields.io/pypi/v/pyforbes.svg)](https://pypi.org/project/pyforbes/) [![Docs](https://readthedocs.org/projects/pyforbes/badge/?version=latest)](https://pyforbes.readthedocs.io/en/latest/) [![Docs](https://img.shields.io/badge/StackOverflow-PyForbes-blue.svg)](https://stackoverflow.com/questions/tagged/pyforbes) [![Docs](https://img.shields.io/pypi/pyversions/pyforbes.svg)](https://pypi.org/project/pyforbes/)

Welcome to the GitHub repository of **PyForbes**

[PyForbes](http://www.github.com/laxmena/PyForbes) is an unofficial Python wrapper for the Forbes API.

PyForbes allows developers to analyze Forbes data and build web applications with this data.

PyForbes provides ease of access to developers and data scientists by providing a Python interface to directly access Forbes data as a [Pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) or JSON Dictionary.

## Installation

Install with `pip`

```
$ pip install pyforbes
```

A Simple PyForbes application typically looks like this

```py
from pyforbes import ForbesList

   flist = ForbesList()

   # Get ForbesList data as a JSON
   billionaires_json = flist.get_json('billionaires', year=2020)

   # Get ForbesList data as a DataFrame
   billionaires_df = flist.get_df('billionaires', year=2020)

   # 30Under30 - Social Media Influencers
   social_media_30 = flist.get_df('30under30-social-media', year=2020)
```

In order to make the most out of PyForbes, you should start
with the [PyForbes Documentation: Examples](https://pyforbes.readthedocs.io/en/latest/examples.html) that will lead you through the most common aspects of the package.

## Documentation

Refer to the documentation, examples and other instructions here: [PyForbes Documentation](https://pyforbes.readthedocs.io/)

## Contributing

Please refer to the [Contribution Guidelines](https://pyforbes.readthedocs.io/en/latest/contribute.html).

![Visitor](https://visitor-badge.laobi.icu/badge?page_id=laxmena.PyForbes)
