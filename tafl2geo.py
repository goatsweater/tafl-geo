import yaml
from pathlib import Path
import sys

import pandas as pd
from shapely.geometry import Point
from geopandas import GeoDataFrame

if __name__ == '__main__':
    data_defn = Path('dataset.yaml')

    if not data_defn.exists():
        sys.exit("Data definition not found. Need dataset.yaml file.")

    with data_defn.open("r") as config:
        cfg = yaml.load(config)

        data_url = Path(cfg['url'])
        if not data_url.exists():
            sys.exit("Data source not found: %s" % data_url.as_posix())
        data_headers = [field['name'] for field in cfg['fields']]

        # read in a little bit of data
        df = pd.read_csv(data_url, header=None, names=data_headers, nrows=20)
        # make a geo dataframe
        geometry = [Point(xy) for xy in zip(df.Longitude, df.Latitude)]
        df = df.drop(['Latitude', 'Longitude'], axis=1)
        crs = {'init': 'epsg:4326'}
        gdf = GeoDataFrame(df, crs=crs, geometry=geometry)

        gdf.to_file(cfg['output'])
