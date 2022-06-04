'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. 

For example:

'abba' & 'baab' == true
'abba' & 'bbaa' == true
'abba' & 'abbba' == false
'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if there are none.

For example:
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
'''

def anagrams(word, words):
    list_symbols = [symbol for symbol in word]
    list_anagrams = []
    for anagram in words:
        check_list = list_symbols.copy()
        if len(anagram) != len(word): continue
        for symbol in anagram:
            if symbol in check_list:
                check_list.remove(symbol)
            else: break
        if len(check_list) == 0: list_anagrams.append(anagram)
    return list_anagrams