Enrich Demo
===========

Setup Data
----------

First, in the ArcGIS Python command prompt, in the directory you want to save the 
demo resources in...

.. code-block:: bash

    git clone https://github.com/knu2xs/business-analyst-python-api-examples
    cd business-analyst-python-api-examples
    make data

This only has to be done once. It puts useful demo data in ``./data/raw/raw.gdb``.

Demonstration
--------------

The Pro project is located at ``./arcigs/business-analyst-python-api-examples``.
Open this Pro project to get started.

Key Messages
^^^^^^^^^^^^^

* Business Analyst is Supporting *Spatial* Data Science Workflows
* Single API for Accessing Business Analyst Data

Open PDX Coffee Demo Map
^^^^^^^^^^^^^^^^^^^^^^^^^

* Enriching *Study Areas* Already Created Surrounding Business Locations

Open ``enrich-demo.ipynb`` Notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

    Set the data path for ``sa_pth`` to where you have this saved on your computer.

    Before doing the demonstration, run the notebook once. This will speed up the results.
    
    After running, clear the results (Cell > All Output > Clear) to be able to run through
    the workflow and have results appear.

    Finally, to make it easier to show progress, you can use ``Shift + Enter`` to execute
    each cell.

* Cell 1 - Imports
    * new capabilities are in the ``enrichment`` module

* Cell 2 - Data Loading
    * Study Areas loaded into Spatially Enabled Data Frame (SEDF)
    * SEDF is Pands Data Frame with additional Spatial property and capabilties added by Esri

* Cell 3 - GIS Source
    * ``GIS`` object instance used to specify source
    * ``'pro'`` keyword used to point to local (ArcGIS Pro + BA + local data pack)

* Cell 4 - Country Discovery
    * Providing the ``GIS`` "source" tells the function where to look for countries, local or remote
    * Available countries discovered and returned as Pandas data frame

* Cell 5 - Create ``Country``
    * Use ISO3 code to create ``Country`` object instance for accessing data available in the Country
    * Signature below informs us the country and the data source in parentheses

* Cell 6 - Discover Available Data
    * ``Country.enrich_variables`` returns a dataframe of all available variables
    * nearly 19,000 in this case

* Cell 7 - Select Analysis Variables
    * Since data frame, all slicing and selection methods are valid
    * Taking advantage of naming conventions to select data to start exploratory analysis
        * Current year (``name`` contains ``'CY'``)
        * Key data collection (``data_collection`` contains ``Key``)

* Cell 8 - Enrich Data
    * Provide study area as a Spatially Enabled Data Frame
    * Can provide enrich variables as filtered data frame - no need for special formatting