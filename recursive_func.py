def func(num):
    if num == 0:
        return 1
    return num * func(num - 2)


print (func(8))
