def myfunc(str):
    print(str)
    nstr = str.lower()
    for i in range(len(str)):
        nstr[i+1].upper()
    return nstr
    
print(myfunc("SlseJbKWdOEuhB"))