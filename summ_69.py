def summer_69(arr):
    summ = 0
    d = 1
    for x in arr:
        if x == 6:
            x = 0
            d = 0
        if x == 9:
            x = 0
            d = 1
        summ = summ + x*d

    return (summ)
print(summer_69([2, 1, 6, 5, 9, 11])) 

