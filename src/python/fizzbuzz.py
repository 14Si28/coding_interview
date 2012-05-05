"""
Fizz buzz aka bizz buzz. 

Count from 0 to 100, replacing any number divisible by 3 with fizz, divisible by 5 with buzz, 
and divisible by both 3 and 5 with fizz buzz.
"""

def fizzbuzz():
    for x in xrange(100):
        if x % 3 == 0 and x % 5 == 0:
            print 'fizz buzz!',
        elif x % 3 == 0:
            print 'fizz',
        elif x % 5 == 0:
            print 'buzz',
        else:
            print x,
        print ', ',
    print

if __name__ == '__main__':
    fizzbuzz()



