"""
Required search inputs: start date, end date, city.
Optional search inputs: price range, room type, keywords (matched against description)
"""
import csv
import re
import datetime
import operator

NONWORDS_RE = re.compile(r'\W+')

IND_AVAILABILITY = 'availability'
IND_PLACE_TO_AVAIL = 'place_id_to_availability_id'
IND_AVAIL_START_DATES = 'avail_start_dates'
IND_AVAIL_END_DATES = 'avail_end_dates'

COL_AVAIL_START_DATE = 2
COL_AVAIL_END_DATE = 3

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
    availability = {}
    avail_by_place = {}
    avail_start_dates = []
    avail_end_dates = []
    for row in csv_rows('data_availability.txt'):
        # [availability_id,place_id,start_date,end_date,price_per_night]
        av_id = row[0]
        place_id = row[1]
        availability[av_id] = row
        
        start_date = parse_date(row[COL_AVAIL_START_DATE])
        row[COL_AVAIL_START_DATE] = start_date
        avail_start_dates.append((start_date, av_id, place_id))

        end_date = parse_date(row[COL_AVAIL_END_DATE])
        row[COL_AVAIL_END_DATE] = end_date
        avail_end_dates.append((end_date, av_id, place_id))

        avail_by_place.setdefault(place_id, []).append(av_id)

    avail_start_dates.sort(key=operator.itemgetter(0))
    avail_end_dates.sort(key=operator.itemgetter(0))

    return {
        IND_AVAILABILITY: availability,
        IND_PLACE_TO_AVAIL: avail_by_place,
        IND_AVAIL_START_DATES: avail_start_dates,
        IND_AVAIL_END_DATES: avail_end_dates
    }

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')

def binsearch(sorted_values, target_value, valfunc=None, select_closest=False, start=-1, end=None, closest=None):
    """
    valfunc: an optional function for extracting the value at sorted_values[index]
    select_closest: when True causes the search to return the closest (inexact) match

    returns: index in sorted_values of the target_value or None if not found
    """
    if not sorted_values or not target_value:
        return None
    if start == -1:
        start = 0
        end = len(sorted_values)-1

    if start > end or end < start:
        if select_closest:
            return closest
        return None # not found

    mid = int((end - start) / 2.0) + start

    if valfunc:
        pivot = valfunc(sorted_values[mid])
    else:
        pivot = sorted_values[mid]

    if target_value == pivot:
        return mid
    elif target_value < pivot:
        return binsearch(sorted_values, target_value, valfunc, select_closest, start=start, end=mid-1, closest=mid)
    # else
    assert target_value > pivot
    return binsearch(sorted_values, target_value, valfunc, select_closest, start=mid+1, end=end, closest=mid)

def available_places(start_date, end_date, avail_start_dates, avail_end_dates):
    """
    returns: set of place_ids of places available during the specified dates
    """
    start_date_index = binsearch(avail_start_dates, start_date, valfunc=operator.itemgetter(0), select_closest=True)
    
    if start_date_index == None:
        return set() # not found

    end_date_index = binsearch(avail_end_dates, end_date, valfunc=operator.itemgetter(0), select_closest=True)

    if end_date_index == None:
        return set() # not found

    start_place_ids = set([x[2] for x in avail_start_dates[0:start_date_index]])
    end_place_ids = set([x[2] for x in avail_end_dates[end_date_index:]])
    
    assert start_place_ids
    assert end_place_ids
    return start_place_ids.intersection(end_place_ids)

def availability_extract(place_ids, start_date, end_date, place_to_avail_index, availability_index):
    if not place_ids:
        return []
    results = []
    for place_id in place_ids:
        av_ids = place_to_avail_index[place_id]
        assert av_ids
        for av_id in av_ids:
            row = availability_index[av_id]
            assert row
            if row[COL_AVAIL_START_DATE] <= start_date and row[COL_AVAIL_END_DATE] >= end_date:
                results.append(row)

    return results

def search(start_date_str, end_date_str, city_name, price_min=None, price_max=None, room_type=None, keywords=None):
    start_date = parse_date(start_date_str)
    end_date = parse_date(end_date_str)
    city_term = normalize(city_name)
    if not city_term:
        raise ValueError('Invalid city. (empty)')

    indexes = build_indexes()
    # Given two dates, find all places available during that range.
    place_ids = available_places(start_date, end_date, indexes[IND_AVAIL_START_DATES], indexes[IND_AVAIL_END_DATES])
    # Given available places and start/end dates, find related availability data (including prices). Price may vary over the start/end range.
    availability = availability_extract(place_ids, start_date, end_date, indexes[IND_PLACE_TO_AVAIL], indexes[IND_AVAILABILITY])
    return availability

def _test_all():
    availability = search('2012-08-08', '2012-08-16', 'san francisco')
    for r in availability:
        print r

if __name__ == '__main__':
    _test_all()

