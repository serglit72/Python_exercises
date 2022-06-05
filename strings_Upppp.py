def accum(s):
    ns = ""
    for i in range(len(s)):
        if i == 0:
            el = s[i].upper()+"-"
            ns += el 
        else:
            el = s[i].upper()+s[i]*i+"-"
            ns += el 
    return ns
# THE BEST SOLUTION

def accum_best(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

def initialize_names(name):
    st = name.split()
    for i in range(1,len(st)-1):
        st[i] = st[i][0]+'.'
    return " ".join(st)   




def cookie(x):
    
    if type(x) == str:
        z = "Zach"
    elif type(x) == float or type(x) == int:
        z = "Monica"
    else : 
        z = "the dog"
    return "Who ate the last cookie? It was "+z+"!" 
def debug0(string: str) -> str:
    """ Remove all instances of the word 'bug' from within a given string, unless the word is plural ('bugs'). """
    from re import sub
    return sub("bug(?!s)", "", string)   

def debug(s):
    #'bugs ooobujgsbugsoobugbugsoo'

    n = s.replace('bugs','----')
    n = n.replace('bug','')
    n = n.replace('----','bugs')
    print(n)

def debug1 (s):
    return s.replace('bugs', '####').replace('bug','').replace('####', 'bugs')

def debug2(s):
    return 'bugs'.join(w.replace('bug', '') for w in s.split('bugs'))

def validate_code(code):
    import re
    return bool(re.match(r"^[123]\d*$",str(code)))

def validate_code2(code):
    import re
    return bool(re.match('[123]',str(code)))
def validate_code3(code):
    return str(code).startswith(('1', '2', '3'))
def validate_code4(code):
    return str(code)[0] in '123'

# Test.assert_equals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
# Test.assert_equals(cookie(2.3), "Who ate the last cookie? It was Monica!")
# Test.assert_equals(cookie(26), "Who ate the last cookie? It was Monica!")
# Test.assert_equals(cookie(True), "Who ate the last cookie? It was the dog!")

# Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 >> [5,4,3,2,1]
def reverseseq(n):
    return range(n, 0, -1)

def validate_pin(pin):
    return pin.isdigit() and (int(pin)%1 == 0 and len(pin) in (4, 6))

def validate_pin2(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1,n+1))

def fly_by(lamps, drone):
    l = drone.count("=")+1
    return lamps.replace("x","o",l)

def xo(s):
    return s.lower().count('x') == s.lower().count('o')


if __name__ == "__main__":
    #print(accum("ZpglnRxqenU"))
    # print(initialize_names('John Ryan selor'))
    print(debug('bugs ooobujgsbugsoobugbugsoo')) #, 
    # print(cookie(2.3))