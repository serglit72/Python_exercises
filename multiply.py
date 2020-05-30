def multiply(numbers): 

    x = 1
    for i in numbers:
        x *= i
        
    return x

print(multiply([1,2,3,-4]))