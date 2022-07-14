"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""

import re


def pig_it(text):
    result = re.sub(r'(\s\W)ay',r'\g<1>',' '.join([(word[1:] + word[0] + 'ay') for word in text.split()]))
    return result
