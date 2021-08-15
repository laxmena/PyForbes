# 🐍 PyForbes - Python wrapper for Forbes API

Welcome to the GitHub repository of **PyForbes**!

[PyForbes](http://www.github.com/laxmena/PyForbes) is an unofficial Python wrapper for Forbes API.

PyForbes allows developers to analyze Forbes data or build web application with Forbes data.

PyForbes provides ease of access to developers and data scientists by providing python interface to directly get the Forbes data as a [Pandas.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) or JSON Dictionary.

A Simple PyForbes application typically looks like this

```
   from pyforbes import ForbesList
   
   flist = ForbesList()

   # Get ForbesList data as a JSON
   billionaires_json = flist.get_json('billionaires', year=2020) 

   # Get ForbesList data as a DataFrame
   billionaires_df = flist.get_df('billionaires', year=2020)
```

In order to make the most out of PyForbes, you should start
with the [PyForbes Documentation: Examples](https://pyforbes.readthedocs.io/en/latest/examples.html) that will lead you through the most common aspects of the package. 

## Documentation
Refer the documentation, examples and other instructions here: [PyForbes Documentation](https://pyforbes.readthedocs.io/)

## Contributing
Please refer the [Contribution Guidelines](https://pyforbes.readthedocs.io/en/latest/contribute.html).
