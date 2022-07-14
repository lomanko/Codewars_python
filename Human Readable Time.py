"""
Write a function, which takes a non-negative integer (seconds) as input
and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

make_readable(0), "00:00:00"
make_readable(5), "00:00:05"
make_readable(60), "00:01:00"
make_readable(86399), "23:59:59"
make_readable(359999), "99:59:59"
"""


# def make_readable(seconds):
#     time = ''
#     for i in range(0, 2):
#         floor_division = seconds // 60
#         modulus = seconds % 60
#         if modulus > 9:
#             time = ':' + str(modulus) + time
#         else:
#             time = ':0' + str(modulus) + time
#         seconds = floor_division
#     modulus = seconds % 100
#     if modulus > 9:
#         time = ':' + str(modulus) + time
#     else:
#         time = ':0' + str(modulus) + time
#     return time[1:]

def make_readable(seconds):
    minutes, seconds = divmod(seconds,60)
    hours, minutes = divmod(minutes,60)
    return ('%02d:%02d:%02d' % (hours,minutes, seconds))