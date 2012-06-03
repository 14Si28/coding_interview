import sys
import csv
import random
import datetime
import argparse

def _property_description():
    return """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

def gen_properties(num_properties=10):
    """
    returns: generator of lists of  [property_id,country_code,city_code,formatted_address,lat,lng,neighborhood_code,room_type,description]
    """
    for next_property_id in xrange(1,num_properties+1):
        
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

def _stay_review():
    return """We had a nice stay. Blah. """ + 'Blah! '*random.randint(1,10)

def gen_ratings(property_ids, min_each=0, max_each=9):
    """
    returns: generator of lists of  [rating_id,property_id,user_id,rating,review]
    """
    next_rating_id = 1
    for property_id in property_ids:
        num_ratings = random.randint(min_each, max_each)
        if num_ratings:
            for r in xrange(num_ratings):
                values = [
                    next_rating_id,
                    property_id,
                    0,
                    random.randint(0,5),
                    _stay_review()
                ]
                next_rating_id += 1
                yield values

def gen_availability(property_ids, min_each=3, max_each=9):
    """
    returns: generator of lists of [availability_id,property_id,start_date,end_date,price_per_night]
    """
    next_availability_id = 1
    max_future_days = 30
    for property_id in property_ids:
        start_date = datetime.date.today() + datetime.timedelta(random.randint(1,30))
        for x in xrange(random.randint(min_each,max_each)):
            end_date = start_date + datetime.timedelta(random.randint(1,max_future_days-1))
            values = [
                next_availability_id,
                property_id,
                start_date,
                end_date,
                random.randint(80,500) 
            ]
            next_availability_id += 1
            start_date = end_date + datetime.timedelta(random.randint(1,10))
            yield values

def gen_property_ids():
    for line in gen_properties():
        yield line[0]

def print_properties(*args):
    writer = csv.writer(sys.stdout)
    property_ids = []
    for line in gen_properties():
        property_ids.append(line[0])
        writer.writerow(line)
    return property_ids

def print_ratings(property_ids):
    writer = csv.writer(sys.stdout)
    for line in gen_ratings(property_ids):
        writer.writerow(line)

def print_availability(property_ids):
    writer = csv.writer(sys.stdout)
    for line in gen_availability(property_ids):
        writer.writerow(line)

TABLE_TYPES = { 'availability': print_availability, 'ratings': print_ratings, 'properties': print_properties }

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--table', default=None, required=True, help='type of data to generate, one of: {}'.format(', '.join(TABLE_TYPES)))
    return parser.parse_args()

def main():
    args = parse_args()
    if not args.table in TABLE_TYPES:
        raise ValueError('Invalid table type: {}'.format(args.table))

    func = TABLE_TYPES[args.table]
    func(gen_property_ids())

if __name__ == '__main__':
    main()

