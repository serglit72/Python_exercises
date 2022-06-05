# middle value index from array of [1,3,2] - value 2 has index 2
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

# basic_op('+', 4, 7)         # Output: 11
# basic_op('-', 15, 18)       # Output: -3
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))

# to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable.\
#  Implement a function that will return minimum number of breaks needed.
def breakChocolate(n, m):
    return n*m-1 if (n > 0 and m > 0) else 0

#Complete the method that takes a boolean value \
# and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    return ('No','Yes')[boolean]

def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)

def is_in_middle(s):
    return is_in_middle(s[1:-1]) if s[4:] else 'abc' in s

def is_in_middle_my(s):
    middle = len(s)//2
    return s[middle-1:middle+2] == "abc" if len(s) % 2 != 0 else s[middle-1:middle+2] == "abc" or  s[middle-2:middle+1] == "abc"

def cat_mouse(x,j):
    try:
        d, c, m = map(x.index,'DCm')
    except ValueError:
        return 'boring without all three'
    if j < abs(c - m)-1 : return 'Escaped!'
    elif c>d>m or m>d>c : return 'Protected!'
    return 'Caught!'

def cat_mouse2(x,j):
    d, c, m = x.find('D'), x.find('C'), x.find('m')
    if -1 in [d, c, m]:
        return 'boring without all three'
    if abs(c - m) <= j:
        return 'Protected!' if c < d < m or m < d < c else 'Caught!' 
    return 'Escaped!'

ef cat_mouse_my(x,j):
    if "C" in x and "D" in x and "m" in x:
        c = x.index('C')
        m = x.index('m')
        d = x.index('D')
        if (d > c and c > m and d > m and abs(m-c)<=j)\
        or (d > c and c < m and d > m and abs(m-c)<=j)\
        or (d < c and c < m and d < m and abs(m-c)<=j)\
        or (d < c and c > m and d < m and abs(m-c)<=j):
            return "Caught!"
#        
        elif abs(c-m) > j:
            return "Escaped!"
        elif (d > c and c < m and d < m) or (d < c and c > m and d > m):
            return "Protected!"

def warn_the_sheep_my(queue):
    if queue != None and "wolf" in queue:
        wolf = queue.index("wolf")
        me = len(queue)-1
        if wolf == me:return 'Pls go away and stop eating my sheep'
        elif wolf < me:return 'Oi! Sheep number '+str(me-wolf)+'! You are about to be eaten by a wolf!'

def warn_the_sheep(queue):
    queue.reverse()
    return 'Pls go away and stop eating my sheep' if queue[0] == 'wolf' else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))  


def greetings(time, name):
    return f"Good {time} {name}" if name and time else 'Hey dude greet someone'
def greetings_my(time, name):
    return "Good "+str(time)+" "+str(name) if not time == None or type(name) == str else "Hey dude greet someone"   

def hello_my(name=None):
    return f"Hello, {name.lower().capitalize()}!" if name else 'Hello, World!'
def hello(name=''):
    return f"hello, {name or 'world'}!".title()

def travel(total_time, run_time, rest_time, speed):
    cycle, left = divmod(total_time, run_time + rest_time)
    return cycle * run_time * speed + min(left, run_time) * speed

def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    plural = '' if diff == 1 else 's'
    if year_of_birth < current_year:
        return 'You are {} year{} old.'.format(diff, plural)
    elif year_of_birth > current_year:
        return 'You will be born in {} year{}.'.format(diff, plural)
    return 'You were born this very year!'

def calculate_age_my(year_of_birth, current_year):
    diff = current_year-year_of_birth
    if diff > 1:
        return f"You are {diff} years old." 
    elif diff < -1 :
        return f"You will be born in {abs(diff)} years."
    elif diff == 0:
        return "You were born this very year!"
    elif diff == 1:
        return "You are 1 year old."
    elif diff == -1:
        return f"You will be born in 1 year."

def set_alarm(employed, vacation):
    return employed and not vacation

def set_alarm_my(employed, vacation):
    
    if employed and vacation:
        return False
    elif (employed == False) and (vacation == True):
        return False
    elif (employed == False) and (vacation == False):
        return False
    elif (employed == True) and (vacation == False):
        return True