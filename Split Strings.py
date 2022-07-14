"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""


def solution(s):
    len_s = len(s)
    list_s = []
    if len_s % 2 != 0: s += '_'
    for symbol in range(0, len(s), 2):
        list_s.append(s[symbol: symbol + 2])
    return list_s
