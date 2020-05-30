def fibonacci(n):
    if n<=1:
        return 1
    return (fibonacci(n-2)+fibonacci(n-1))

def print_fibonacci(n):
    for i in range(n): 
        print(fibonacci(i))

print(print_fibonacci(10))