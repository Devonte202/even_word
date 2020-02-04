"""
Problem: Given a string find out how many letters need to be removed to make that string an 'even word'
input: string
output: number(integers)

Examples: 
even_word('aaaa') == 0
even_word('potato') == 2
even_word('aabbbb') == 0
even_word('aaabbbccc') == 3

Data Structure: Dictionary 
Algorithm: 
0: Create an empty dictionary and a variable initialized with 0
1: loop through the string, enter each letter into the dictionary
2: Loop through dictionary
    I: Check to see which letters have odd values
    II: For those letters decrement the value by one to make it even
    III: In this loop add to the remove_count variable
3: Return the remove_count variable
"""

def even_word(word):
    word_log = {}
    remove_count = 0
    for letter in word:
        if letter in word_log:
            word_log[letter] += 1
        if letter not in word_log:
            word_log[letter] = 1
            
    for letter in word_log:
        if word_log[letter] % 2 != 0:
            word_log[letter] -= 1
            remove_count += 1
        
    return remove_count
    
print(even_word('aaaa'))
print(even_word('potato'))
print(even_word('aabbbb'))
print(even_word('aaabbbccc'))