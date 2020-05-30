# return the difference between the largest and smallest 
# values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions 
# return the smaller or larger of two values.

# 1 method:

def big_diff(nums):
    if len(nums) != 0:
        nums.sort()
        d = nums[-1]-nums[0]
        return d
    return 0

# method 2
def big_diff(nums):
    if len(nums) != 0:
        
