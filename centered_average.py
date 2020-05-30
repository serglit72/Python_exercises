def centered_average(nums):
    if len(nums)>=3:
        nums.sort()
        del nums[0]
        nums.pop()
        
        summ = 0
    
        if nums[0] == nums[1]:
            del nums[0]
        elif nums[-1] == nums[-2]:
            del nums[-1]
    
        for i in range(len(nums)):
            summ =summ+nums[i]
        return int(summ/len(nums)-1)
    return 0
print (centered_average([-10, -4, -2, -4, -2, 0]))