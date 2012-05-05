"""
Secret Santa problem: exchange of presents among a group. 
Given a list of names, each person gives one present to one other person. 
Everyone must give only one present, and each must receive one present. 
The exchange cannot be reciprocal, e.g. if person A gives to B, B cannot give to A. 

Create an algorithm that, as randomly as possible, assigns givers and recipients.

Then prove that it works correctly.
"""

import random

def secretsanta_shuffle(attendees):
    """
    O(n)
    In this solution, we randomize the list of attendees, 
    then sequentially assign recipients using the next in the random list.
    This is cheating but simple. It does not correctly prevent reciprocal assignment.
    Python's shuffle uses the Fisher-Yates algo which is O(n).
    """
    if not attendees:
        return {}

    if len(attendees) <= 1:
        return { attendees[0]: attendees[0] }

    random.shuffle(attendees)
    assignments = {}
    for ind in xrange(len(attendees)-1):
        assignments[attendees[ind]] = attendees[ind+1]

    assignments[attendees[len(attendees)-1]] = attendees[0]
    return assignments


def secretsanta_ugly(attendees):
    """
    O(n^2)
    
    This ugly solution tracks givers and recipients separately, 
    randomly choosing pairs from the remaining list.
    The ugliness lies in special casing a few of the assignments.

    """
    if not attendees:
        return {}

    # A single attendee happily gives presents to his or herself.
    if len(attendees) <= 1:
        return { attendees[0]: attendees[0] }

    # There's no way to prevent reciprocal assignment if there are only 2 attendees.
    if len(attendees) == 2:
        return { attendees[0]: attendees[1], attendees[1]: attendees[0] }

    attendees = sorted(attendees)
    givers = list(attendees)
    recipients = list(attendees)
    assignments = {}
    while givers or recipients:
        assert len(recipients) == len(givers)
        if len(givers) == 1:
            # When there is only one attendee left, we patch the assignment to create a three way assignment.
            k = assignments.iterkeys().next()
            recip = assignments[k]
            assignments[k] = givers[0]
            assignments[givers[0]] = recip
            break
        elif len(givers) == 3 and givers == recipients:
            # When there are only three attendees left, there are only 2 ways to assign correctly.
            if random.randint(0,1) == 0:
                assignments[givers[0]] = givers[1]
                assignments[givers[1]] = givers[2]
                assignments[givers[2]] = givers[0]
            else:
                assignments[givers[0]] = givers[2]
                assignments[givers[2]] = givers[1]
                assignments[givers[1]] = givers[0]
            break
        else:
            # Randomly assign a giver to a recipient.
            # Limit the attempts to prevent an infinite loop.
            ATTEMPT_LIMIT = 1000
            for x in xrange(ATTEMPT_LIMIT):
                gindex = random.randint(0, len(givers)-1)
                rindex = random.randint(0, len(recipients)-1)
                give = givers[gindex]
                receive = recipients[rindex]
                # Prevent the disallowed cases:
                # A - B  # recipriocal assignment
                # B - A
                # C - C  # self assign
                if give != receive and (not receive in assignments or assignments[receive] != give):
                    assignments[give] = receive
                    givers.pop(gindex)
                    recipients.pop(rindex)
                    break
            if x >= ATTEMPT_LIMIT-1:
                raise Exception('Massive fail. Givers: {}   Recipients: {}'.format(givers, recipients))

    assert len(assignments) == len(attendees)
    return assignments


def _test_secretsanta(f, attendees):
    for x in xrange(1000):
        f(attendees)

    # TODO Assertions!
    actual = f(attendees)
    if attendees:
        print f
        print attendees
        print actual
        print '________'
        assert actual

def _test_all(f):
    _test_secretsanta(f, ['Alice', 'Bob', 'Carl', 'Doug'])
    _test_secretsanta(f, ['Alice', 'Bob', 'Carl', 'Doug', 'Elisa', 'Frank', 'George'])
    _test_secretsanta(f, [])
    _test_secretsanta(f, ['Alice'])
    _test_secretsanta(f, ['Alice', 'Bob'])
    _test_secretsanta(f, ['Alice', 'Bob', 'Carl'])

if __name__ == '__main__':
    _test_all(secretsanta_shuffle)
    _test_all(secretsanta_ugly)

