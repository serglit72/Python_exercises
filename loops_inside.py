#There is enough money available on ATM in nominal value 10, 20, 50, 100, 200 and 500 dollars.
#You are given money in nominal value of n with 1<=n<=1500.
#Try to find minimal number of notes that must be used to repay in dollars, or output -1 if it is impossible.

def solve_my(n):
    x=0
    while n > 0:
        if n>= 500 or n %500 == 0:
            x += 1
            n -= 500
        elif n >= 200 or n % 200 == 0:
            x +=1
            n -= 200
        elif n >= 100 or n % 100 == 0:
            x +=1
            n -= 100
        elif n>= 50 or n % 50 == 0:
            x += 1
            n -= 50
        elif n >= 20 or n %20 == 0:
            x +=1
            n -= 20
        elif n >= 10 or n % 10 == 0:
            x +=1
            n -=10
        else:
            return -1
    return x   

def solve(n):
    if n % 10 != 0: return -1
    count=0
    arr = [500,200,100,50,20,10]
    for el in arr:
        while n >= el:
            n -= el
            count += 1
    return count


def get_sum_my(a,b):
    if b-a == 1  or a == b:
        return 1
    elif b - a == -1:
        return -1
    else: 
        s = 0
        for x in range(min(a, b), max(a, b) + 1):
            s += x
    return s

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

def seven_my(m):
    n = 0
    if m == 0: return 0,0
    if m < 99 and m % 7 == 0:
        return m,1
    else:
        while m//100 > 0:
            m = m//10 - m%10*2
            n += 1         
    return m,n

def arithmetic_sequence_sum_my(a, r, n):
    result = 0
    for i in range(n):
        result += a + i*r
    return result

def arithmetic_sequence_sum(a, r, n):
    return sum(a + r*n for n in range(n))

# print(arithmetic_sequence_sum(3, 2, 20))
# print(arithmetic_sequence_sum(2, 3, 5))

def coin_combo_my(cents):
    coins = [25,10,5,1]
    returns = []
    while cents > 0:
        for el in coins:
            c = cents//el
            returns.append(c)
            cents -= c*el
    return returns[::-1]    

def coin_combo(cents):
    out = []
    for i in (25,10,5,1):
        n, cents = divmod(cents, i)
        out.append(n)
    return out[::-1]

def coin_combo_2(cents):
    return [cents%5, ((cents%25)%10)//5, (cents%25)//10, cents//25] 

def sum1_bad_solution(array):
    a = []
    print(len(array))
    for x in array:
        ind_x = array.index(x)+1
        a.append(x*ind_x)
    return sum(a) 
    
def sum1_good(array):
    return sum(val*ind_x for ind_x,val in enumerate(array,1))  


def longest(words):
    return max([len(x) for x in words])

# def solved(arr):
#     a = []
#     x = 0
#     for each in arr:
#         for i,letter in enumerate(each):
#             i = ord(letter)
#             if first <= next:
#                 x+=1
#         a.append(x)
#     return a 

def solvedd(arr):
    a = []
    b = []
    n = 0
    for each in arr:
        for i,letter in enumerate(each):
            x =ord(letter)
            a.append(x)
        for y in range(len(a)+1):
            if a[y]<=a[y+1]:
                n+=1
        b.append(n)
    return b                  

def chetno(arr):
   
    return [el for el in arr if not el % 2]

# def find_digit(num, nth):
#     a = [x for x in str(num) if st == nth]
#     return st

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

def tower_builder(n_floors):
    s = n_floors *2 -1
    return [str("*" * x).center(s," ") for x in range(1,s+1,2)]

def toCsvText(array) :
    '''
    input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
    
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
    '''
   return '\n'.join(','.join(str(n) for n in lst) for lst in array)


def solve_arr(arr):
    return [n for i,n in enumerate(arr) if all(n > x for x in arr[i + 1:])]

def solve_arr_my(arr):
    dominant =[]
    dom = 0
    for each in reversed(arr):
        
        if each > dom:
            dom = each
            dominant.append(dom)
            
    return dominant[::-1]

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))