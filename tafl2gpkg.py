import argparse
import csv
from pathlib import Path
import sys

import osgeo.ogr as ogr
import osgeo.osr as osr

def add_field(layer, field_name, field_type, field_width):
    """Add a field to the layer."""
    field = ogr.FieldDefn(field_name, field_type)
    field.SetWidth(field_width)
    layer.CreateField(field)

def set_field(feature, name, value):
    """Set the value in a field for the feature."""
    #print("{}: {}".format(name, value))
    feature.SetField(name, value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert TAFL CSV data to geopackage.')
    parser.add_argument('input', help='Path to input TAFL CSV file.')
    parser.add_argument('output', help='Path to output GPKG file.')

    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)

    # ensure paths don't conflict
    if not in_path.exists():
        sys.exit("Invalid input path.")

    if out_path.exists():
        sys.exit("Output file already exists.")

    with open(in_path, newline='') as in_file:
        reader = csv.reader(in_file)

        # create the output gpkg
        driver = ogr.GetDriverByName("GPKG")
        data_source = driver.CreateDataSource(out_path.as_posix())

        srs = osr.SpatialReference()
        srs.ImportFromEPSG(4326)

        # create the layer
        layer = data_source.CreateLayer("tafl", srs, ogr.wkbPoint)

        # add all the fields
        add_field(layer, "Radio_Type", ogr.OFTString, 2)
        add_field(layer, "Frequency_MHZ", ogr.OFTReal, 4)
        add_field(layer, "Frequency_record_identifier", ogr.OFTString, 10)
        add_field(layer, "Regulatory_service", ogr.OFTString, 10)
        add_field(layer, "Communication_type", ogr.OFTString, 4)
        add_field(layer, "Conformity_to_freq_plan", ogr.OFTString, 10)
        add_field(layer, "Frequency_allocation_name", ogr.OFTString, 50)
        add_field(layer, "Channel", ogr.OFTString, 10)
        add_field(layer, "International_coordination_number", ogr.OFTString, 20)
        add_field(layer, "Analog_digital", ogr.OFTString, 1)
        add_field(layer, "Occupied_bandwidth_khz", ogr.OFTString, 20)
        add_field(layer, "Designation_of_emission", ogr.OFTString, 20)
        add_field(layer, "Modulation_type", ogr.OFTString, 13)
        add_field(layer, "Filtration_installed", ogr.OFTString, 5)
        add_field(layer, "Tx_effective_radiated_power_dbw", ogr.OFTString, 10)
        add_field(layer, "Tx_transmitter_power_w", ogr.OFTString, 40)
        add_field(layer, "Total_losses_db", ogr.OFTString, 10)
        add_field(layer, "Analog_capacity", ogr.OFTString, 20)
        add_field(layer, "Digital_capacity", ogr.OFTString, 20)
        add_field(layer, "Rx_unfaded_received_signal_level_dbw", ogr.OFTString, 15)
        add_field(layer, "Rx_threshold_signal_level_for_BER_dbw", ogr.OFTString, 15)
        add_field(layer, "Manufacturer", ogr.OFTString, 70)
        add_field(layer, "Model_number", ogr.OFTString, 100)
        add_field(layer, "Antenna_gain_dbi", ogr.OFTString, 15)
        add_field(layer, "Antenna_pattern", ogr.OFTString, 6)
        add_field(layer, "Half_power_beam_width_deg", ogr.OFTString, 4)
        add_field(layer, "Front_back_ratio_db", ogr.OFTString, 5)
        add_field(layer, "Polarization", ogr.OFTString, 1)
        add_field(layer, "Height_AGL_m", ogr.OFTString, 10)
        add_field(layer, "Azimuth_main_lobe_deg", ogr.OFTString, 10)
        add_field(layer, "Vertical_elevation_angle_deg", ogr.OFTString, 10)
        add_field(layer, "Station_location", ogr.OFTString, 200)
        add_field(layer, "Licensee_station_reference", ogr.OFTString, 100)
        add_field(layer, "Call_sign", ogr.OFTString, 10)
        add_field(layer, "Type_of_station", ogr.OFTString, 2)
        add_field(layer, "ITU_class", ogr.OFTString, 2)
        add_field(layer, "Station_cost_category", ogr.OFTString, 2)
        add_field(layer, "Num_identical_stations", ogr.OFTString, 5)
        add_field(layer, "Reference_id", ogr.OFTString, 100)
        add_field(layer, "Province", ogr.OFTString, 2)
        add_field(layer, "Latitude", ogr.OFTReal, 12)
        add_field(layer, "Longitude", ogr.OFTReal, 12)
        add_field(layer, "Ground_elevation_MSL_m", ogr.OFTString, 10)
        add_field(layer, "Antenna_structure_height_AGL_m", ogr.OFTString, 10)
        add_field(layer, "Congestion_zone", ogr.OFTString, 1)
        add_field(layer, "Radius_of_operation_km", ogr.OFTString, 7)
        add_field(layer, "Satellite_name", ogr.OFTString, 1)
        add_field(layer, "Authorization_number", ogr.OFTString, 13)
        add_field(layer, "Service", ogr.OFTString, 1)
        add_field(layer, "Subservice", ogr.OFTString, 3)
        add_field(layer, "Licence_type", ogr.OFTString, 1)
        add_field(layer, "Authorization_status", ogr.OFTString, 2)
        add_field(layer, "In_service_date", ogr.OFTDate, 10)
        add_field(layer, "Account_number", ogr.OFTString, 12)
        add_field(layer, "Licensee_name", ogr.OFTString, 200)
        add_field(layer, "Licensee_address", ogr.OFTString, 200)
        add_field(layer, "Operational_status", ogr.OFTString, 1)
        add_field(layer, "Station_class", ogr.OFTString, 1)
        add_field(layer, "Horizontal_power_w", ogr.OFTString, 50)
        add_field(layer, "Vertical_power_w", ogr.OFTString, 50)
        add_field(layer, "Standby_transmitter_information", ogr.OFTString, 1)

        try:
            print("Loading data...")
            for row in reader:
                if reader.line_num == 333920:
                    print("Skipping line 333920")
                    continue
                #print("----- Row {} -----".format(reader.line_num))
                # convert the row to a feature
                feature = ogr.Feature(layer.GetLayerDefn())
                # Set the attributes from the CSV file
                set_field(feature, "Radio_Type", row[0])
                set_field(feature, "Frequency_MHZ", row[1])
                set_field(feature, "Frequency_record_identifier", row[2])
                set_field(feature, "Regulatory_service", row[3])
                set_field(feature, "Communication_type", row[4])
                set_field(feature, "Conformity_to_freq_plan", row[5])
                set_field(feature, "Frequency_allocation_name", row[6])
                set_field(feature, "Channel", row[7])
                set_field(feature, "International_coordination_number", row[8])
                set_field(feature, "Analog_digital", row[9])
                set_field(feature, "Occupied_bandwidth_khz", row[10])
                set_field(feature, "Designation_of_emission", row[11])
                set_field(feature, "Modulation_type", row[12])
                set_field(feature, "Filtration_installed", row[13])
                set_field(feature, "Tx_effective_radiated_power_dbw", row[14])
                set_field(feature, "Tx_transmitter_power_w", row[15])
                set_field(feature, "Total_losses_db", row[16])
                set_field(feature, "Analog_capacity", row[17])
                set_field(feature, "Digital_capacity", row[18])
                set_field(feature, "Rx_unfaded_received_signal_level_dbw", row[19])
                set_field(feature, "Rx_threshold_signal_level_for_BER_dbw", row[20])
                set_field(feature, "Manufacturer", row[21])
                set_field(feature, "Model_number", row[22])
                set_field(feature, "Antenna_gain_dbi", row[23])
                set_field(feature, "Antenna_pattern", row[24])
                set_field(feature, "Half_power_beam_width_deg", row[25])
                set_field(feature, "Front_back_ratio_db", row[26])
                set_field(feature, "Polarization", row[27])
                set_field(feature, "Height_AGL_m", row[28])
                set_field(feature, "Azimuth_main_lobe_deg", row[29])
                set_field(feature, "Vertical_elevation_angle_deg", row[30])
                set_field(feature, "Station_location", row[31])
                set_field(feature, "Licensee_station_reference", row[32])
                set_field(feature, "Call_sign", row[33])
                set_field(feature, "Type_of_station", row[34])
                set_field(feature, "ITU_class", row[35])
                set_field(feature, "Station_cost_category", row[36])
                set_field(feature, "Num_identical_stations", row[37])
                set_field(feature, "Reference_id", row[38])
                set_field(feature, "Province", row[39])
                set_field(feature, "Latitude", row[40])
                set_field(feature, "Longitude", row[41])
                set_field(feature, "Ground_elevation_MSL_m", row[42])
                set_field(feature, "Antenna_structure_height_AGL_m", row[43])
                set_field(feature, "Congestion_zone", row[44])
                set_field(feature, "Radius_of_operation_km", row[45])
                set_field(feature, "Satellite_name", row[46])
                set_field(feature, "Authorization_number", row[47])
                set_field(feature, "Service", row[48])
                set_field(feature, "Subservice", row[49])
                set_field(feature, "Licence_type", row[50])
                set_field(feature, "Authorization_status", row[51])
                set_field(feature, "In_service_date", row[52])
                set_field(feature, "Account_number", row[53])
                set_field(feature, "Licensee_name", row[54])
                set_field(feature, "Licensee_address", row[55])
                set_field(feature, "Operational_status", row[56])
                set_field(feature, "Station_class", row[57])
                set_field(feature, "Horizontal_power_w", row[58])
                set_field(feature, "Vertical_power_w", row[59])
                set_field(feature, "Standby_transmitter_information", row[60])

                # create the point
                lat = row[40] or 0
                long = row[41] or 0
                wkt = "POINT({} {})".format(float(long), float(lat))
                point = ogr.CreateGeometryFromWkt(wkt)

                # set feature geometry
                feature.SetGeometry(point)

                # create the feature in the layer
                layer.CreateFeature(feature)
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
        except IndexError as e:
            print('Invalid record index on line {}'.format(reader.line_num))
            print(row)
            sys.exit(e)
