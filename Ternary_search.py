def guessNumber(n):
    right = n  
    left = 1
    while left <= right:
        m1 = left+(right-left)/3
        m2 = right-(right-left)/3
    
        num1 = guess(m1)
        num2 = guess(m2)
        if num1 == 0:
            return m1
        if num2 == 0:
            return m2
        elif num1 == -1:
            right = m1 - 1
        elif num2 == 1:
            left = m2 + 1
        else: 
            left = m1 + 1
            right = m2 -1
    return m1

