###You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

# Input Format

# Example 1 Input: coins = [1,2,5], amount = 11 Output: 3 Explanation: 11 = 5 + 5 + 1

# Example 2 Input: coins = [2], amount = 3 Output: -1

# Example 3 Input: coins = [1], amount = 0 Output: 0

# Example 4 Input: coins = [1], amount = 1 Output: 1

# Example 5 Input: coins = [1], amount = 2 Output: 2

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
    if coins == 0: return 0
    if coins == 1 and amount == 0: return 0
    counter = []
    arr = sorted(coins)
   
    for i in range(len(arr)-1,-1,-1):
        if amount % arr[i] == 0 or amount/arr[i] == 1:
            r = amount//arr[i]
            counter.append(r)
            return int(counter[0])

        else:    
            rest = amount % arr[i]
            r = amount//arr[i]
            if r>0:
                counter.append(r)
                amount = rest
    x = 0
    for j in range(len(counter)):
        x += int(counter[j])
    return (x)

amount = 17
coins = [1,2,5]
print (count(coins, amount))