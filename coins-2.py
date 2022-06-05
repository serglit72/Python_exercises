import math
import os
import random
import re
import sys

#
# Complete the 'count' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY coins
#  2. INTEGER amount
#

def count(coins, amount):
    #
    # Write your code here
    # Function should return only one number - answer
    #
    len_coins = len(coins)
    if not coins or amount < min(coins): return -1
    if coins[0] == 0: return 0
    if len_coins == 1 and amount == 0: return 0
    if len_coins >=1 and len_coins <=12:
        for coin in coins:
            if coin == amount:
                return 1
    else:
        return -1
    counter = []
    x = 0
    rest = None
    
   
    while (len(coins)>0 and rest != 0):
        one = max(coins)
    
        if amount % one == 0 or amount/one == 1:
            r = amount//one
            counter.append(r)
            coins.pop()
            rest = amount % one
            amount = rest

        else:    
            rest = amount % one
            r = amount//one
            if rest>0:
                counter.append(r)
                amount = rest
            coins.pop()
    if not counter:
        return 
    else:
        for j in range(len(counter)):
            x += int(counter[j])
    return x
    
amount = 1
coins = [1,2,3,4,5,6,7,8,9,10,11,12,15,20,30]
print (count(coins, amount))