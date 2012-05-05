"""
Secret Santa problem: exchange of presents among a group. 
Given a list of names, each person gives one present to one other person. 
Everyone must give only one present, and each must receive one present. 
The exchange cannot be reciprocal, e.g. if person A gives to B, B cannot give to A. 

Create an algorithm that, as randomly as possible, assigns givers and recipients.

Then prove that it works correctly.
"""

import random

def secretsanta(attendees):
    if not attendees or len(attendees) <= 1:
        return {}

    if len(attendees) == 2:
        return { attendees[0]: attendees[1], attendees[1]: attendees[0] }

    attendees = sorted(attendees)
    givers = list(attendees)
    recipients = list(attendees)
    assignments = {}
    while givers or recipients:
        assert len(recipients) == len(givers)
        if len(givers) == 1:
            k = assignments.iterkeys().next()
            tmp = assignments[k]
            assignments[k] = givers[0]
            assignments[givers[0]] = tmp
            break
        elif len(givers) == 3 and givers == recipients:
            assignments[givers[0]] = givers[1]
            assignments[givers[1]] = givers[2]
            assignments[givers[2]] = givers[0]
            break
        else:
            limit = 1000
            for x in xrange(limit):
                gindex = random.randint(0, len(givers)-1)
                rindex = random.randint(0, len(recipients)-1)
                give = givers[gindex]
                receive = recipients[rindex]
                if give != receive and (not receive in assignments or assignments[receive] != give):
                    assignments[give] = receive
                    givers.pop(gindex)
                    recipients.pop(rindex)
                    break
            if x >= limit-1:
                print attendees
                print givers
                print recipients
                raise Exception('Massive fail.')

    assert len(assignments) == len(attendees)
    return assignments

if __name__ == '__main__':
    for x in xrange(1000):
        print secretsanta(['Alice', 'Bob', 'Carl', 'Doug'])
        print secretsanta(['Alice', 'Bob', 'Carl', 'Doug', 'Elisa', 'Frank', 'George'])
        print secretsanta([])
        print secretsanta(['Alice'])
        print secretsanta(['Alice', 'Bob'])
        print secretsanta(['Alice', 'Bob', 'Carl'])

