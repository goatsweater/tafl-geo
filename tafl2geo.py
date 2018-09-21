import argparse
from pathlib import Path
import sys

import pandas as pd
from shapely.geometry import Point
from geopandas import GeoDataFrame, io

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="TAFL CSV file.")
    parser.add_argument('output', help="Path to geopackage")
    args = parser.parse_args()

    # ensure the input file exists
    infile = Path(args.input)
    if not infile.exists():
        sys.exit("Could not find input file")

    outfile = Path(args.output)
    if not outfile.suffix.lower() == '.gpkg':
        sys.exit("Geopackages must have a .gpkg extension")

    # TAFL doesn't have headers on the data, so we need to specify them
    # adding the data type makes dealing with the data easier
    schema = {'Radio Type': 'object', 'Frequency': 'float64', 'Frequency record identifier': 'float64', 'Regulatory service': 'float64', 'Communication type': 'object', 'Conformity to frequency plan': 'object', 'Frequency allocation name': 'object', 'Channel': 'object', 'International coordination number': 'object', 'Analog digital': 'object', 'Occupied bandwidth': 'object', 'Designation of emission': 'object', 'Modulation type': 'object', 'Filtration installed': 'object', 'TX effective radiated power': 'object', 'TX transmitter power': 'object', 'Total losses': 'float64', 'Analog capacity': 'object', 'Digital capacity': 'object', 'RX unfaded received signal level': 'object', 'RX threshold signal level for BER': 'object', 'Manufacturer': 'object', 'Model number': 'object', 'Antenna gain': 'float64', 'Antenna pattern': 'object', 'Half power beam width': 'object', 'Front back ratio': 'float64', 'Polarization': 'object', 'Height AGL': 'float64', 'Azimuth main lobe': 'object', 'Vertical elevation angle': 'float64', 'Station location': 'object', 'Licensee station reference': 'object', 'Call sign': 'object', 'Type of station': 'float64', 'ITU class': 'object', 'Station cost object': 'float64', 'Number identical stations': 'object', 'Reference id': 'object', 'Province': 'object', 'Latitude': 'float64', 'Longitude': 'float64', 'Ground elevation MSR': 'object', 'Antenna structure height AGL': 'float64', 'Congestion zone': 'object', 'Radius of operation': 'object', 'Satellite name': 'float64', 'Authorization number': 'object', 'Service': 'object', 'Subservice': 'object', 'License type': 'object', 'Authorization status': 'object', 'In service date': 'object', 'Account number': 'object', 'Licensee name': 'object', 'Licensee address': 'object', 'Operational status': 'object', 'Station class': 'object', 'Horizontal power': 'object', 'Vertical power': 'object', 'Standby transmitter information': 'float64'}

    headers = [h for h in schema]

    # read in a little bit of data
    df = pd.read_csv(infile, header=None, names=headers, dtype=schema, low_memory=False)

    # make a geo dataframe
    geometry = [Point(xy) for xy in zip(df.Longitude, df.Latitude)]
    df = df.drop(['Latitude', 'Longitude'], axis=1)
    crs = {'init': 'epsg:4326'}
    gdf = GeoDataFrame(df, crs=crs, geometry=geometry)
    # fill in missing values
    #gdf.fillna('Unknown')

    # prep and write the output
    #io.file.infer_schema(gdf)
    gdf.to_file(outfile, driver='GPKG', layer='tafl')
