"""
Licensing

Copyright 2020 Esri

Licensed under the Apache License, Version 2.0 (the "License"); You
may not use this file except in compliance with the License. You may
obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing
permissions and limitations under the License.

A copy of the license is available in the repository's
LICENSE file.
"""
import sys
from pathlib import Path

import arcpy

dir_src = Path(__file__).parent
sys.path.append(str(dir_src))

from demo_data import demo_data, DataAsset

__all__ = ['make_data']

arcpy.env.overwriteOutput = True


def make_data():

    dir_data = dir_src.parent/'data'

    dir_raw = dir_data/'raw'
    dir_int = dir_data/'interim'
    dir_out = dir_data/'processed'
    dir_ext = dir_data/'external'
    dir_lst = [dir_raw, dir_int, dir_out, dir_ext]

    for data_dir in dir_lst:
        if not data_dir.exists():
            data_dir.mkdir(parents=True)

    gdb_raw = dir_raw/'raw.gdb'
    gdb_int = dir_int/'interim.gdb'
    gdb_out = dir_out/'processed.gdb'
    gdb_ext = dir_ext/'external.gdb'
    gdb_lst = [gdb_raw, gdb_int, gdb_out, gdb_ext]

    for gdb in gdb_lst:
        if not arcpy.Exists(str(gdb)):
            arcpy.management.CreateFileGDB(str(gdb.parent), str(gdb.name))

    for itm in demo_data:
        if isinstance(itm, DataAsset):
            itm.df.spatial.to_featureclass(str(gdb_raw/itm.name))


if __name__ == '__main__':
    make_data()

