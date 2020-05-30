import collections


a_great_sentence = "The bird is the word"

######## 1. Each character occurence counting using loop:
char_occurence = dict()

for i in a_great_sentence:
    if i in char_occurence:
        char_occurence[i]+=1
    else:
        char_occurence[i]=1
print("Counter",char_occurence)

######### 2.  Used "collections.Counter()" library


easy_char_occurence = collections.Counter(a_great_sentence)

print(easy_char_occurence)

######### 3. Using "dict.get()"
'''
get() method is used to check the previously occurring character in string, 
if its new, it assigns 0 as initial and appends 1 to it, 
else appends 1 to previously holded value of that element in dictionary.
'''

get_char_occurence = {}

for keys in a_great_sentence:
    get_char_occurence[keys] = get_char_occurence.get(keys, 0)+1

print("Counter",get_char_occurence)    

######### #4 : Using set() + count()
'''
count() coupled with set() can also achieve this task, in this we just iterate 
over the set converted string and get the count of each character in original string 
and assign that element with that value counted using count().
/// The count() method returns the number of times a specified value appears in the string.
SYNTAX: string.count(value, start, end) 
EX: x = txt.count("apple", 10, 24) - search from position 10 to 24
/// set() - is unordered and unindexed BUT you can loop through the set items using a "for" loop, 
or ask if a specified value is present in a set, by using the "in" keyword.

'''
set_count_char_occurence = {i : a_great_sentence.count(i) for i in set(a_great_sentence)}

print("Counter",set_count_char_occurence)