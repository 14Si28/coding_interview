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
    if len(attendees) <= 1:
        return {}

    # if len(attendees) == 2:
    #     return { attendees[0]: attendees[1], attendees[1]: attendees[0] }

    # if len(attendees) == 3:
    #     return { attendees[0]: attendees[1], attendees[1]: attendees[2], attendees[2]: attendees[0] }

    givers = list(attendees)
    recipients = list(attendees)
    assignments = {}
    while givers or recipients:
        while True:
            gindex = random.randint(0, len(givers)-1)
            rindex = random.randint(0, len(recipients)-1)
            give = givers.pop(gindex)
            receive = recipients.pop(rindex)
            if give != receive and (not receive in assignments or assignments[receive] != give):
                assignments[give] = receive
                break

    return assignments


if __name__ == '__main__':
    print secretsanta(['Alice', 'Bob', 'Carl', 'Doug', 'Elisa', 'Frank', 'George'])
    print secretsanta(['Alice'])
    print secretsanta(['Alice', 'Bob'])
    print secretsanta(['Alice', 'Bob', 'Carl'])

