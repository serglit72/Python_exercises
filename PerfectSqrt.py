def isPerfectSquare(num):
    if num <= 1:
        return True
    
    left = 2
    right = num
    print("right = ",right)
    while left <= right:
        m = (left+right)//2
        print ("m = ",m)
        if left * left == num:
            return True
        elif left * left < right:
            left = m+1
            print("left = ", left)
        else:
            right = m-1
            print("right_new = ", right)
    return False

print(isPerfectSquare(121))