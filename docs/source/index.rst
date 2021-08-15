.. PyForbes documentation master file, created by
   sphinx-quickstart on Sun Aug 15 11:43:50 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyForbes - Python wrapper for Forbes API
========================================

.. note::
   This project is under active development.

.. toctree::
   :hidden:

   intro.rst
   install.rst
   examples.rst
   supported_lists.rst
   contribute.rst
   development.rst
   support.rst

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

