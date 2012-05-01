"""
Convert a remaining time in seconds to its components (remaining hours, minutes, seconds).
"""

#         hours   mins  seconds
delta_s = 60*60*8+60*38+18

# TODO Simplify?
hours = int(delta_s / (60*60))
minutes = int((delta_s % (60*60))/60)
seconds = delta_s - (hours*60*60 + minutes*60)

print '{}s =  {}:{}:{}   (hours:minutes:seconds)'.format(delta_s, hours, minutes, seconds)
