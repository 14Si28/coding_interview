import sys
import csv
import random
import datetime

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

def gen_availability(property_ids):
    """
    returns: generator of lists of [availability_id,property_id,start_date,end_date,price_per_night]
    """
    next_availability_id = 1
    max_future_days = 30*6 # ~6 months
    for property_id in property_ids:
        start_date = datetime.date.today() + datetime.timedelta(random.randint(1,30))
        end_date = start_date + datetime.timedelta(random.randint(1,max_future_days-1))
        values = [
            next_availability_id,
            property_id,
            start_date,
            end_date,
            random.randint(80,500) 
        ]
        next_availability_id += 1
        yield values

def print_properties():
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

def main():
    property_ids = print_properties()
    print_ratings(property_ids)
    print_availability(property_ids)

if __name__ == '__main__':
    main()

