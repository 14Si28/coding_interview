import sys
import csv

def _property_description():
    return """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

def gen_properties(num_properties=10):
    for next_property_id in xrange(1,num_properties+1):
        # property_id,country_code,city_code,formatted_address,lat,lng,neighborhood_code,room_type,description
        values = [
            next_property_id,
            'us',
            'sf',
            '500 Sansome',
            0,
            0,
            'castro',
            'entire_apt',
            _property_description()
        ]
        yield values

def print_properties():
    writer = csv.writer(sys.stdout)
    for line in gen_properties():
        writer.writerow(line)

def main():
    print_properties()

if __name__ == '__main__':
    main()

