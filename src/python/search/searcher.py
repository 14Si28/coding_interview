"""
Required search inputs: start date, end date, city.
Optional search inputs: price range, room type, keywords (matched against description)
"""
import csv
import re
import datetime

NONWORDS_RE = re.compile(r'\W+')

def csv_rows(filename):
    with open(filename) as input_file:
        reader = csv.reader(input_file)
        for row in reader:
            yield row

def normalize(term):
    norm = re.sub(NONWORDS_RE, '', term)
    norm = norm.lower()
    return norm

def build_indexes():
    csv_rows('data_places.txt')  
    pass

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')

def search(start_date, end_date, city_name, price_min=None, price_max=None, room_type=None, keywords=None):
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    city_term = normalize(city_name)
    if not city_term:
        raise ValueError('Invalid city. (empty)')

    build_indexes()


def _test_all():
    search('2012-08-08', '2012-08-16', 'san francisco')

if __name__ == '__main__':
    _test_all()

