'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. 
It should return true if the string is valid, and false if it's invalid.

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?

A string of braces is considered valid if all braces are matched with the correct brace.

Examples

"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''

def valid_braces(string):
    braces_list = ['()', '[]', '{}']
    while len(string) > 1:
        if '()' in string: 
            string = string.replace('()','')
        elif '{}' in string: 
            string = string.replace('{}','')
        elif '[]' in string: 
            string = string.replace('[]','')
        else:
            break
    if len(string) > 0:
        return False
    else:
        return True
