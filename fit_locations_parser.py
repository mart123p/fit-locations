#!/usr/bin/env python3 
#-----------------------------------------------------------------------------------------------
# Garmin FIT Locations Intepreter
#-----------------------------------------------------------------------------------------------
#
# Description:
#   Reads `Lctns.fit` and outputs the locations to stdout.
#
#   Arran Smith
#   Created: 2020-08-19
#
#   Martin Pouliot (Console output changes)
#   Modified: 2021-07-27
#
#-----------------------------------------------------------------------------------------------

import sys
import argparse
import fitparse
from tabulate import tabulate
class FitReader:

    def __init__(self):
        self.location_message = "unknown_29"
        self.field_mapping = {
            "name": "unknown_0",
            "id": "unknown_254",
            "longitude": "unknown_2",
            "latitude": "unknown_1",
            "icon": "unknown_4",
        }
    
    def read(self, filename):

        # Load the FIT file

        # https://pythonhosted.org/fitparse/api.html
        fitfile = fitparse.FitFile(filename)

        # Iterate over all messages of type "record"
        # (other types include "device_info", "file_creator", "event", etc)
        table = []
        table.append(["Name", "Coordinates", "Latitude", "Longitude"])
        table.append([])
        for record in fitfile.get_messages(self.location_message):

            fit_message = {}
            # Records can contain multiple pieces of data (ex: timestamp, latitude, longitude, etc)
            for data in record:
            
                # Skip empty data
                if data.value is None:
                    continue

                for key, value in self.field_mapping.items():
                    if data.name == value:
                        if data.name == self.field_mapping["longitude"] or data.name == self.field_mapping["latitude"]:
                            # Garmin saves the position as a 32Bit Signed Int
                            # https://gis.stackexchange.com/questions/371656/garmin-fit-coodinate-system/371667#371667

                            fit_message[key] = data.value / (2**32 / 360)
                        else:
                            fit_message[key] = data.value
            
            coordinates = "{},{}".format(fit_message["latitude"], fit_message["longitude"])
            table.append([fit_message["name"], coordinates, fit_message["latitude"], fit_message["longitude"]])
        
        print(tabulate(table))

if __name__ == '__main__':
    parser = argparse.ArgumentParser("fit_locations_parser", description='Parse FIT locations files')
    parser.add_argument("-i", "--input", help="FIT input file location", type=str, required=True)

    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    FitReader().read(args.input)
