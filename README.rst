.. image:: https://img.shields.io/pypi/v/pyforbes.svg
   :target: https://pypi.org/laxmena/pyforbes

.. image:: https://readthedocs.org/projects/pyforbes/badge/?version=latest
  :target: https://pypi.org/laxmena/pyforbes

.. image:: https://img.shields.io/badge/StackOverflow-PyForbes-blue.svg
   :target: https://stackoverflow.com/questions/tagged/pyforbes

.. image:: https://img.shields.io/pypi/pyversions/pyforbes.svg
   :target: https://pypi.org/laxmena/pyforbes

Welcome to the GitHub repository of PyForbes!

`PyForbes <http://www.github.com/laxmena/PyForbes>`_ is a unofficial Python 
wrapper for Forbes API.

PyForbes allows developers to analyze Forbes data or build web 
application with Forbes data.

PyForbes provides ease of access to developers and data scientists by 
providing python interface to directly get the Forbes data as a 
`Pandas.DataFrame <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_ or JSON Dictionary.

A Simple PyForbes application typically looks like this

.. code-block:: python

   from pyforbes import ForbesList
   
   flist = ForbesList()

   # Get ForbesList data as a JSON
   billionaires_json = flist.get_json('billionaires', year=2020) 

   # Get ForbesList data as a DataFrame
   billionaires_df = flist.get_df('billionaires', year=2020)

In order to make the most out of PyForbes, you should start
with the :ref:`examples <examples>` that will lead you through the most common
aspects of the package. 
