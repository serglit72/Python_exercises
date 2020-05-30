def sum13(nums):
    if len(nums) != 0:
        summ = 0
        for i in range(len(nums)):
            if nums[i] != 13:
                summ = summ + nums[i]
            elif nums[i] == 13:
                summ = summ -nums[i-1]
        return summ
    return 0
print (sum13 ([1, 2, 2, 1, 13]))