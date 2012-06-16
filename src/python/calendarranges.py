"""
Given a calendar with appointments (start and end times), find all the conflicting appointments. (Overlapping start end times.) When multiple appointments conflict over the same time window (30 minute intervals), return all conflicting appointments as a distinct list.

For example:
Appointments:
A  10:00 - 11:30
B  11:00 - 12:30
C  10:30 - 1:00
D  1:00 - 2:00
E  1:30 - 2:30
F  3:00 - 3:30  

Returns conflicts:
A, B, C  10:30 - 11:30
B, C 11:00 - 12:30
D, E 1:30 - 2:00
"""

# Possible approaches: interval trees, sorting by start time, binning...
#
# http://www.biostars.org/post/show/2244/what-is-the-quickest-algorithm-for-range-overlap/
# http://www.biostars.org/post/show/99/fast-interval-intersection-methodologies/
# https://bitbucket.org/james_taylor/bx-python/src/tip/lib/bx/intervals/intersection.pyx
# http://en.wikipedia.org/wiki/R-tree
#

import operator

def _start(appt):
    return appt[1]

def _end(appt):
    return appt[2]

def _name(appt):
    return appt[0]

def find_conflicts_naive(appointments):
    """
    O(n^2) time complexity. Not a good answer.
    """
    def _appt_key(left, right):
        key = [_name(left), _name(right)]
        key = sorted(key)
        return '{},{}'.format(*key)

    results = []
    seen = set()
    for x in appointments:
        for y in appointments:
            if x == y:
                continue
            key = _appt_key(x, y)
            if not key in seen:
                seen.add(key) # prevent duplicates
                if _start(y) < _end(x) and _end(y) >= _start(x):
                    tmp = [x,y]
                    tmp = sorted(tmp, key=operator.itemgetter(1))
                    results.append(tmp)

    return results


def find_conflicts_naive2(appointments):
    """
    O(n) time complexity. This is not a generalized solution. 
    This does not correctly collapse the resulting conflict time ranges. (It reports half hour time intervals.)
    """
    results = []
    schedule = [None,] * (24*2) # 24 hours * 2 for half hour intervals

    def _timeslots(appt):
        start = int(_start(appt) * 2)
        end = int(_end(appt) * 2)
        return xrange(start, end)

    def _from_timeslot(timeslot):
        return timeslot / 2.0

    # Create a schedule at each half hour time interval.  O( 48 * n ) => O(n)
    # If the appointment times were sorted, we could skip to the first appointment time interval, and stop at the last.
    for x in appointments:
        for t in _timeslots(x):
            if schedule[t] == None:
                schedule[t] = []

            schedule[t].append(x)

    conflicts = []
    seen = set()
    for i in xrange(len(schedule)):
        # Any time slot that has more than one appointment has a conflict.
        if schedule[i] and len(schedule[i]) > 1:
            key = ','.join([_name(z) for z in schedule[i]])
            if not key in seen:
                seen.add(key) # prevent duplicates
                print 'Conflict @ {} : {}'.format(_from_timeslot(i), schedule[i])
                conflicts.append(schedule[i])

    return conflicts


##################################


APPOINTMENTS2 = [
    ('a', 10, 11.5),
    ('b', 11, 12.5),
    ('c', 10.5, 13),
    ('d', 13, 14),
    ('e', 13.5, 14.5),
    ('f', 15, 15.5)
]

APPOINTMENTS1 = [
    ('a', 10, 11.5),
    ('b', 11, 12.5),
    ('c', 13, 15)
]



def _test_all(func):
    print func(APPOINTMENTS1)
    print func(APPOINTMENTS2)

if __name__ == '__main__':
    _test_all(find_conflicts_naive)
    _test_all(find_conflicts_naive2)
    
