Setup and Configuration
=======================

If you just want to get started and not be encumbered by reading much background, just do the following from
the command line in a location where you want to save this repo. If you are using Conda packaged with ArcGIS
Pro, you will need to ensure you open the command prompt from Start > ArcGIS > Python Command Prompt.

.. code-block:: bash

    git clone https://github.com/knu2xs/business-analyst-python-api-examples
    cd business-analyst-python-api-examples
    make env  ::Optional on Windows with ArcGIS Pro
    make data
    jupyter lab ./notebooks

From there, take a look at and try the example notebooks.

Requirements
############

At a minimum, you will need some version of Conda to work with. If you want to run the examples referencing
local resources, you will need ArcGIS Pro with Business Analyst and the United States data pack installed.
Most of the time I try to explicitly call out where I am using local resources, and if you switch these to
reference remote (typically ArcGIS Online), the examples will work.

.. warning::

    Using ArcGIS Online for enrichment costs credits, so please be aware of this!

Conda
#####

Conda is a Python environment and packaging system. When installing ArcGIS Pro, this is how Python is run.
Conda is installed with ArcGIS Pro, but Conda is *not* added to the system paths. This means the ``conda``
comamands will *not* work unless you start the command prompt from Start > ArcGIS > Python Command Prompt.

However, if you have installed either miniconda or Anaconda on your system *and* have also installed ArcGIS
Pro, you *should* have Conda added to your system path. All of the ``make`` commands should work for this
configuration as well.

Creating Conda Environments
###########################

These notebooks depend on a Conda environment, and although I make no gaurantees, I try to ensure if any extra
requirements, additional Python packages, are needed, they are included in the ``environments.yml`` file.
Further, since Conda environment creation is repetitive, I have created a way to streamline getting the Conda
environment set up. This is the ``make env`` command above. This accesses a section of the ``./make.bat`` script
copying the ArcGIS Pro default environment ``arcgispro-py3``, and adds additional packages listed in the
``environments.yml`` file.
