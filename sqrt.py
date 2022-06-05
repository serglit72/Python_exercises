
def mySqrt(x):
    if(x==0):
        return 0
    right = x
    left = 0
    if right <=2 :
        return 1
    if right > 10:
        left == 10
    if (right > 2):   
        while left <= right:
            m = (left+right)//2
            if (m * m == x):
                return m
            if m * m < x:
                left = m + 1
            else: 
                right = m - 1
        return right
print(mySqrt(10))