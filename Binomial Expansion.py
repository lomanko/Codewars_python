"""
The purpose of this kata is to write a program that can do some algebra.
Write a function expand that takes in an expression with a single, one character variable, and expands it.
The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative,
x is any single character variable, and n is a natural number. If a = 1,
no coefficient will be placed in front of the variable.

If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f...
where a, c, and e are the coefficients of the term, x is the original one character variable
that was passed in the original expression and b, d, and f, are the powers that x is being raised
to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included.
If the coefficient of a term is one, the coefficient should not be included.
If the coefficient of a term is -1, only the "-" should be included.
If the power of the term is 0, only the coefficient should be included.
If the power of the term is 1, the caret and power should be excluded.

Examples:
expand("(x+1)^2")      # returns "x^2+2x+1"
expand("(p-1)^3")      # returns "p^3-3p^2+3p-1"
expand("(2f+4)^6")     # returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
expand("(-2a-4)^0")    # returns "1"
expand("(-12t+43)^2")  # returns "144t^2-1032t+1849"
expand("(r+0)^203")    # returns "r^203"
expand("(-x-1)^2")     # returns "x^2+2x+1"
"""
import re


def factorial(number):
    n_factorial = 1
    while number > 1:
        n_factorial *= number
        number -= 1
    return n_factorial


def c_n_k(n, k):
    return factorial(n)/(factorial(k) * factorial(n - k))


def elements(expr):
    first_el = re.search(r'(\-*\d*)(\w+)', expr).group()
    second_el = re.search(r'[\+-]\d+\)', expr).group()
    if len(first_el) == 1:
        return [1, first_el, int(second_el[:-1])]
    else:
        return [int(first_el[:-1]), first_el[-1], int(second_el[:-1])]


def expand(expr):
    level = int(expr[-1])
    if level == 0:
        return '1'
    if level == 1:
        return expr[1:level-4]
    list_elements = elements(expr)

    first_el = list_elements[0] ** level
    if first_el == 1:
        first_el = ''
    first_el = str(first_el) + str(list_elements[1]) + '^' + str(level)
    result = first_el
    for i in range(1, level):
        c_n_k_1 = c_n_k(level, i)
        a = elements(expr)[1] + '^' + str(level-i)
        a_int = elements(expr)[0] ** (level-i)
        b = elements(expr)[2] ** i
        new_el = str(int(c_n_k_1 * a_int * b)) + str(a)
        if new_el[0] != '-':
            result += '+'
        result = result + new_el
    last_el = list_elements[2] ** level
    if last_el > 0:
        result += '+'
    result += str(last_el)

    result = result.replace('^1', '')
    return result
