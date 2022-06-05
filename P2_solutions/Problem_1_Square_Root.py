
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if(number==0):
        return 0
    right = number
    left = 0
    if right <=2 :
        return 1
    if right > 10:
        left == 10
    if (right > 2):   
        while left <= right:
            m = (left+right)//2
            if (m * m == number):
                return m
            if m * m < number:
                left = m + 1
            else: 
                right = m - 1
        return right


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")