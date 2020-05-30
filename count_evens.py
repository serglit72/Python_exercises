def count_evens(nums):
    if len(nums)!=0:
        n = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                n+=1
        return n
    return 0

print(count_evens([2,1, 2, 3, 4]))