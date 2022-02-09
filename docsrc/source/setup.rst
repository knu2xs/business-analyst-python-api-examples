Setup and Configuration
=======================

If you just want to get started and not be encumbered by reading much background, just do the following from
the command line in a location where you want to save this repo. If you are using Conda packaged with ArcGIS
Pro, you will need to ensure you open the command prompt from Start > ArcGIS > Python Command Prompt.

.. code-block:: batch

    git clone https://github.com/knu2xs/business-analyst-demos
    cd business-analyst-demos
    make env
    jupyter lab

From there, take a look in the ``./notebooks`` directory to find the example notebooks.

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
environment set up. If you *are not* internal to Esri and helping with development, this process is 
comparatively easy. If you *are* helping with development, I have tried to make it as painless as possible.

Creating an Environment with Stable
***********************************

If all you need to do is get set up with the stable branch, your live is comparatively straightforward. The
four lines above will get you started. These commands retrieve the contents of this repository to your local
machine, steps into the directory, creates a Conda environment named ``ba-demos``, installs dependencies, and 
starts Jupyter Lab so you can investigate the example notebooks in the ``./notebooks`` directory.

Creating an Environment with a Development Branch
*************************************************

If you have access to the development repository, this means you are internal to Esri and likely are helping
out with development or testing of the Python API. To make your life a little easier as well, you can run
these following commands.

.. code-block:: batch

    git clone https://github.com/knu2xs/business-analyst-demos
    cd business-analyst-demos
    make get-geosaurus
    make env-geosaurus
    jupyter lab

This clones the development branch of the Python API into the ``./src`` directory on your machine, creates
an environment named ``geosaurus-demos`` with the same dependences from the ``environment.yml`` file and
installs the downloaded development version of the Python API using PIP in edit mode. This means if you 
need to switch to a different branch or pull updates for any reason, Python will recognize these changes,
and you can immediately test against them. 