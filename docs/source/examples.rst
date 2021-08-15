.. _examples:

Examples
---------

Following examples will walk you through how to use the PyForbes package.

PyForbes supports fetching data for 60+ Forbes Lists. You can find the 
supported ForbesList here: :ref:`PyForbes Supported ForbesLists Index <supported_lists>`


.. contents::
   :depth:  4

Example 1: Get ForbesList data    
###############################

The following example demonstrates how to get data for a specific Forbes List.
We can get the data in three different data-types **request.response**, 
**pandas.DataFrame** and **dict**(JSON).

.. code-block:: python
   :linenos:

   from pyforbes import ForbesList

    flist = ForbesList()
    # Get Data as requests.response datatype
    richest400_res = flist.get_response("forbes-400")

    # Get Data as Pandas DataFrame
    richest400_df = flist.get_df("forbes-400")

    # Get Data as JSON Dict
    richest400_json = flist.get_json("forbes-400")

Example 2: Get ForbesList data for a specific year
##################################################

You can also fetch ForbesList data for a specific year.
Similar to the previous example, we can get the data in three different 
data-types **request.response**, **pandas.DataFrame** and **dict**(JSON).

.. code-block:: python
   :linenos:

   from pyforbes import ForbesList

    flist = ForbesList()
    # Get Data as requests.response datatype for the year 2016
    richest400_res = flist.get_response("forbes-400", year=2016)

    # Get Data as Pandas DataFrame for the year 2017
    richest400_df = flist.get_df("forbes-400", year=2017)

    # Get Data as JSON Dict for the year 2018
    richest400_json = flist.get_json("forbes-400", year=2018)

