from functools import lru_cache
from pathlib import Path

from arcgis.features import GeoAccessor
import pandas as pd


class DataAsset(object):

    def __init__(self, path: Path) -> None:
        self.path = path
        self.name = path.stem

    def __repr__(self):
        return f'<DataAsset - {self.name}>'

    @property
    @lru_cache(128)
    def df(self):
        df = pd.read_pickle(self.path)
        keep_cols = [c for c in df.columns if
                     'fips' in c.lower()
                     or 'id' in c.lower()
                     or c == 'SHAPE'
                     or c.lower() == 'locnum']
        df = df.loc[:, keep_cols]
        df.spatial.set_geometry('SHAPE')
        return df

    def to_feature_class(self, output_gdb: Path):
        return self.df.spatial.to_featureclass(str(output_gdb/self.name))


class DemoData(object):

    def __init__(self):

        data_dir = Path(__file__).parent/'pkl_files'
        for pkl_pth in data_dir.glob('*pkl'):
            setattr(self, pkl_pth.stem, DataAsset(pkl_pth))

    @property
    def assets(self):
        asset_lst = [itm for itm in self.__dict__.values() if isinstance(itm, DataAsset)]
        return asset_lst

demo_data = DemoData()
