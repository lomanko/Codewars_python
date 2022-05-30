'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized 
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
'''

def to_camel_case(text):
    camel_text = ''
    if text:
        if '-' or '_' in text:
            camel_text = text[0]
            for symbol in range(1,len(text)):
                if text[symbol - 1] == "-" or text[symbol - 1] == "_":
                    camel_text += text[symbol].capitalize()
                else:
                    camel_text += text[symbol]
    camel_text = camel_text.replace('_','')
    camel_text = camel_text.replace('-','')
    return camel_text