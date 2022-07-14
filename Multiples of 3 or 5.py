"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


def solution(number):
    if number:
        sum_of_multiples = sum([i for i in range(1, number) if (i % 3 == 0) or (i % 5 == 0)])
    else:
        sum_of_multiples = 0
    return sum_of_multiples
