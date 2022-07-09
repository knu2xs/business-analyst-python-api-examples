from functools import lru_cache
from typing import Union, List, Optional

from arcgis.geoenrichment import Country
from arcgis.geometry import Polygon
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

__all__ = ['EnrichBase', 'EnrichPolygon', 'EnrichStandardGeography', 'KeepOnlyEnrichColumns', 'ArrayToDataFrame']


class EnrichBase(BaseEstimator, TransformerMixin):
    """
    The ``arcpy.geoenrichment.Country.enrich`` method provides access to a massive
    amount of data for analysis, a treasure trove of valuable data you can use
    through enrichment. This object streamlines the process of accessing this
    method as part of a SciKit-Learn Pipeline by wrapping the functionality
    into a Transformer, specifically a preprocessor, and is used to create
    other transformers performing more specific tasks.
    """

    _country = None
    _enrich_variables = None
    _return_geometry = None

    def __int__(self, country: Country, enrich_variables: Union[List[str], pd.DataFrame],
                return_geometry: bool = True) -> None:
        """
        Args:
            country: Country to be used for enrichment.
            enrich_variables: A list of enrich variable names or filtered dataframe of enrich variables to be used.
            return_geometry: Do you want the shapes or not?
        """
        # apply the parent init methods to get standard methods such as get and set params for free
        super().__init__()

        self.country = country
        self.enrich_variables = enrich_variables
        self.return_geometry = return_geometry

    @property
    def country(self):
        """``arcgis.geoenrichment.Country`` object instance being used."""
        return self._country

    @country.setter
    def country(self, country: Country):
        assert isinstance(country, Country)
        self._country = country

    @property
    def enrich_variables(self):
        """Pandas data frame of variables being used for enrichment."""
        return self._enrich_variables

    @enrich_variables.setter
    def enrich_variables(self, enrich_variables: Union[List[str], pd.DataFrame]):
        # use a trick, reaching into the Country to get a matching method, to get a dataframe if only a list
        if isinstance(enrich_variables, list):
            self._enrich_variables = self.country._ba_cntry.get_enrich_variables_from_iterable(enrich_variables)
        elif isinstance(enrich_variables, pd.DataFrame):
            self._enrich_variables = enrich_variables
        else:
            raise ValueError('enrich_variables must be either a list of enrich variable names or a enrich variable '
                             'data frame')

    @property
    def return_geometry(self):
        """Do you want the geometry when enriching?"""
        return self._return_geometry

    @return_geometry.setter
    def return_geometry(self, return_geometry: bool):
        assert isinstance(return_geometry, bool)
        self._return_geometry = return_geometry

    @property
    @lru_cache(maxsize=8)
    def enrich_var_aliases(self):
        """List of enrich aliases, so you can understand what the variables are."""
        return list(self.enrich_variables['alias'])

    def fit(self, X):
        """Since just building a preprocessor nothing is happening here."""
        return self


class EnrichPolygon(EnrichBase):
    """
    The ``arcpy.geoenrichment.Country.enrich`` wrapped in a preprocessor
    for enriching input areas delineated with ``arcgis.geometry.Polygon``
    geometries. Inherits from ``EnrichBase``.
    """

    def __init__(self, country: Country, enrich_variables: Union[List[str], pd.DataFrame],
                 return_geometry: bool = True) -> None:
        """
        Args:
            country: Country to be used for enrichment.
            enrich_variables: A list of enrich variable names or filtered dataframe of enrich variables to be used.
            return_geometry: Do you want the shapes or not?
        """
        super().__init__(country, enrich_variables, return_geometry)

    def transform(self, X: Union[pd.DataFrame, List[Polygon], np.ndarray]) -> pd.DataFrame:
        """
        Retrieve Pandas Data Frame of enriched data.

        Args:
            X: List of Polygon geometries or Spatially Enabled DataFrame of areas
                to be enriched.

        Returns:
            Enriched data.
        """
        # since just for polygons, make sure this is what we are working with
        has_valid_polygons = False

        if isinstance(X, pd.DataFrame):
            if X.spatial.name is not None:
                if X.spatial.validate():
                    geom_typ_lst = X.spatial.geometry_type
                    if len(geom_typ_lst):
                        geom_typ = geom_typ_lst[0]
                        if geom_typ.lower() == 'polygon':
                            has_valid_polygons = True

        elif isinstance(X, (list, np.ndarray)):
            first_geom = X[0]
            if first_geom.geometry_type.lower() == 'polygon':
                has_valid_polygons = True

        if not has_valid_polygons:
            raise ValueError('It does not appear the inputs are valid Polygons. Please ensure the inputs are valid '
                             'Polygons.')

        # invoke enrich and put in variable to make debugging easier
        ret_df = self.country.enrich(X, enrich_variables=self.enrich_variables, return_geometry=self.return_geometry)

        return ret_df


class EnrichStandardGeography(EnrichBase):
    """
    The ``arcpy.geoenrichment.Country.enrich`` wrapped in a preprocessor
    for enriching a list of standard geographies identified by their
    unique identifiers. A common example is postal or ZIP codes.
    """

    _standard_geography_level = None

    def __init__(self, country: Country, enrich_variables: Union[List[str], pd.DataFrame], standard_geography_level=str,
                 return_geometry: bool = True) -> None:
        """
        Args:
            country: Country to be used for enrichment.
            enrich_variables: A list of enrich variable names or filtered dataframe of enrich variables to be used.
            standard_geography_level: Standard geography level to use for enrichment.
            return_geometry: Do you want the shapes or not?
        """
        super().__init__()

        # set properties
        self.country = country
        self.enrich_variables = enrich_variables
        self.standard_geography_level = standard_geography_level
        self.return_geometry = return_geometry

    @property
    def standard_geography_level(self):
        return self._standard_geography_level

    @standard_geography_level.setter
    def standard_geography_level(self, standard_geography_level):
        assert isinstance(standard_geography_level, str)
        assert standard_geography_level in list(self.country.levels['level_name'])
        self._standard_geography_level = standard_geography_level

    def transform(self, X: Union[pd.DataFrame, List[Polygon], np.ndarray]) -> pd.DataFrame:
        """
        Retrieve Pandas Data Frame of enriched data.

        Args:
            X: List of standard geography unique identifiers.

        Returns:
            Enriched data.
        """
        # only accepting list or numpy array of input ids
        assert isinstance(X, (list, np.ndarray)), "Enrich input must be a list."

        # also, must all be strings
        is_str_lst = [isinstance(val, str) for val in X]
        assert all(is_str_lst), "Standard geography identifiers must be strings."

        # invoke enrich and put in variable to make debugging easier
        ret_df = self.country.enrich(X, enrich_variables=self.enrich_variables,
                                     standard_geography_level=self.standard_geography_level,
                                     return_geometry=self.return_geometry)

        return ret_df


class KeepOnlyEnrichColumns(BaseEstimator, TransformerMixin):
    """
    Remove any non-enrich variable columns from a Pandas data frame.
    """

    keep_columns_ = None

    def __init__(self, country: Country, id_column: Optional[str] = None, keep_geometry: bool = True):
        """
        Args:
            country: ``arcgis.geoenrichment.Country`` object used for original enrichment.
            id_column: Column with unique identifiers. This will become the output index. If no column specified, the
                existing index will be used.
            keep_geometry: Whether to keep the geometry, if applicable.
        """
        super().__init__()

        self.country = country
        self.id_column = id_column
        self.keep_geometry = keep_geometry

    def fit(self, X: pd.DataFrame):
        """
        Sets properties based on the input parameters and data.

        Args:
            X: Pandas data frame created from the ``arcgis.geoenrichment.Country.enrich`` method.

        Returns:
            Pandas DataFrame pruned to just retain columns from enrichment.
        """
        # create a list of columns in compiled list - have to check two different columns
        for nm_col in ['name', 'enrich_field_name']:

            # get a list of potential values - all lowercase
            col_nm_lst = list(self.country.enrich_variables[nm_col].str.lower())

            # compare column names to potential values and only keep the matching ones
            self.keep_columns_ = [c for c in X.columns if c.lower() in col_nm_lst]

            # if something found, quit looking
            if len(self.keep_columns_):
                break

        return self

    def transform(self, X: pd.DataFrame):
        """
        Args:
            X: Pandas data frame output from ``arcgis.geoenrichment.Country.enrich`` method.
        Returns:
            Pandas data frame with only enrich columns, the identifier column as the index, and the geometry column,
            if applicable.
        """
        # if an id column is provided, set as the index
        if self.id_column:
            assert self.id_column in X.columns, "The id_column must be a column in the input_dataframe."
            X = X.set_index(self.id_column, drop=True)

        # if geometry is desired in the output, add it to the column name list, and flat
        keep_cols = self.keep_columns_
        set_geometry = False
        geom_col = None
        if self.keep_geometry:
            if X.spatial.validate():
                set_geometry = True
                geom_col = X.spatial.name
                keep_cols.append(geom_col)

        # drop any columns not in list
        out_df = X.loc[:, keep_cols]

        # if keeping geometry column, make sure GeoAccessor recognizes it
        if set_geometry:
            assert geom_col is not None
            out_df.spatial.set_geometry(geom_col)

        return out_df


class ArrayToDataFrame(BaseEstimator, TransformerMixin):
    """
    Helper to convert the output ``np.ndarray`` back into a
    Pandas DataFrame.
    """
    def __init__(self, columns_template: Union[pd.DataFrame, List[str]], index: Optional[list] = None) -> None:
        """
        Args:
            columns_template: Template of columns to use when creating the data frame.
            index: Index to add on data frame.
        """

        self.columns_template = columns_template
        self.index = index

        self.n_features_in_ = None

        if isinstance(columns_template, pd.DataFrame):
            self.feature_names_in_ = columns_template.columns
        else:
            self.feature_names_in_ = columns_template

    def fit(self, X: np.ndarray):
        """
        Fit method, which just sets properties.
        Args:
            X: ``np.ndarray`` to be converted into a Pandas Data Frame.
        """
        self.n_features_in_ = len(X)
        assert X.shape[1] == len(self.feature_names_in_), (
            f'X column count: {X.shape[1]} != column name count: {len(self.feature_names_in_)}'
        )

        if self.index is not None:
            assert X.shape[0] == len(self.index)

        return self

    def transform(self, X: np.ndarray):
        """
        Convert the ``np.ndarray`` into a Pandas DataFrame.

        Args:
            X: ``np.ndarray`` to be converted into a Pandas Data Frame.

        Returns:
            Data from the ``nd.ndarray`` in the columns from the Pandas Data Frame.
        """
        if isinstance(X, pd.DataFrame):
            X_df = X

        elif self.index is None:
            X_df = pd.DataFrame(X, columns=self.feature_names_in_)

        else:
            X_df = pd.DataFrame(X, columns=self.feature_names_in_, index=self.index)

        return X_df
