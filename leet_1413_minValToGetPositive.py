# 1413. Minimum Value to Get Positive Step by Step Sum
# the code works,but not very fast, need improvement
# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Input: nums = [-3,2,-3,4,2]
# Output: 5

def minInitial(nums):
    if min(nums) >= 0:
        return 1
    
    start = 0
    for num in nums:
        start += abs(num)
    
    
    
    while start > 0:
        print("start is ",start)
        prefix = [nums[0]+start]
        for i in range(1, len(nums)):
            prefix.append( prefix[-1] + nums[i])
        print('prefix :',prefix)
        if min(prefix)>1 and start > 1:
            print("too big")
            start -= 1
            continue
        break
    return start

# nums = [-3,2,-3,4,2]
# nums = [1,-2,-3]
# nums = [1,2]
# nums = [2,3,5,-5,-1]
nums = [-3,2,-3,4,2]


print(minInitial(nums))


    


    

    
