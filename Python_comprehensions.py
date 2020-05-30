'''
Comprehensions are a convenient way to work with iterables in Python.
 Comprehensions let you skip the for loop and start creating lists, dicts, and sets 
 straight from your iterables. Comprehensions also let you emulate functional programming
aspects like map() and filter() in a more accessible way. 
'''

# Example
################   list comprehension

x = [num * 2 for num in range(1, 6)]
#>>> [2, 4, 6, 8, 10, 12]

################   dict comprehension

d = {letter: num for letter, num in zip('abcdef', range(1, 7))}
#>>> {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

################    set comprehension

s= {num * 2 for num in [5, 2, 18, 2, 42, 2, 2]}
#>>> {84, 10, 4, 36}

#You can select only certain elements by adding an "if" condition:
line_list = ['  line 1\n', 'line 2  \n', ...]
stripped_list = [line.strip() for line in line_list if line != ""]

# generator example

seq1 = 'abc'
seq2 = (1, 2, 3)
# Syntax error
[x, y for x in seq1 for y in seq2]
# Syntax correct
[(x, y) for x in seq1 for y in seq2]  
# >>>[('a', 1), ('a', 2), ('a', 3),
# >>> ('b', 1), ('b', 2), ('b', 3),
# >>> ('c', 1), ('c', 2), ('c', 3)]