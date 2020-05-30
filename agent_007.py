def spy_game(nums):
    # d = 0
    for i in range(len(nums)):
        if nums[i] == 0 and nums[i+1] == 0:
            if nums[i+2] == 7:
                return True

print(spy_game([1,2,4,0,0,2,5,7,0,0,1,0,7,5]))