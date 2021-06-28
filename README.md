# FIT Locations Parser

Watches such as the Garmin Instinct store saved locations in a `FIT` file called `Lctns.fit`, However this file is 
treated differently to other `FIT` files on the device - So processing with other FIT utilities is not possible.

This python script **ONLY** converts `Lctns.fit` from a Garmin device into a console format.
## Requirements

- [fitparse](https://github.com/dtcooper/python-fitparse)
- [tabulate](https://github.com/astanin/python-tabulate)

## Usage

```
usage: fit_locations_parser [-h] -i INPUT

Parse FIT locations files

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        FIT input file location
```
## Attribution
Original work comes from [Arran-nz](https://github.com/arran-nz) and his repository [fit-geojson](https://github.com/arran-nz/fit-geojson). I have changed the script to output the content directly to stdout in a human readable format.