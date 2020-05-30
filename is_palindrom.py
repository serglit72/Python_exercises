def palindrom(s):
    '''
    recursion here is to check the last and the first char in given string
    we consider the palindrom if we have " " or "a" (empty char or only one char)
    so "sedes" is palindrom but "sledes" is not
    '''
    if len(s)<=1: #check if we have only 1 char or " "
        return True
    if s[0] != s[-1]: #check if the first and last char NOT EQUAL
        return False
    return palindrom(s[1:-1]) 

print(palindrom('weereew'))
