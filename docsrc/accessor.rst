Data Frame Accessor
===================

Pandas includes the ability to `extend the Data Frame object capabilities`_ using the
concept of accessors, custom namespaces as a property of the ``DataFrame`` object. In
the Python API for ArcGIS, the ``spatial`` namespace is an accessor, the GeoAccessor
object registered using the to use the *spatial* namespace using the
`register_dataframe_accessor`_ decorator method. This same paradigm can be used to
create a ``ba`` (Business Analyst) namespace where we can put an ``enrich`` method.

.. _extend the Data Frame object capabilities: https://pandas.pydata.org/docs/development/extending.html
.. _register_dataframe_accessor: https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html