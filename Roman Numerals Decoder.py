'''
Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, 
starting with the leftmost digit and skipping any 0s. 
So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). 
The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:
solution('XXI') # should return 21

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''

def solution(roman):
    symbol_values = {'M': 1000, 'D': 500 , 'C': 100 , 'L': 50 , 'X': 10 , 'V': 5, 'I': 1}
    decimal_value = [0]
    values_list = [symbol_values[symbol] for symbol in roman]
    index = 0
    for item in values_list[-1::-1]:
        if item >= decimal_value[index]:
            decimal_value.append(item)
            index += 1
        else:
            decimal_value[index] -= item
    return sum(decimal_value)  

