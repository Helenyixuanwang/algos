# 1413. Minimum Value to Get Positive Step by Step Sum


# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Input: nums = [-3,2,-3,4,2]
# Output: 5

# a faster and more effecient method, I wrote it after I read the explanation from the platform
def minInitial(nums):
    # the first element in the prefix array must be "0" zero because when all numbers in the 
    # array are positive, the start value must be "1". At that time, the minVal should be zero
    # so that "1" could be returned. If the prefix = [ nums[0]], the test cases will  fail when 
    # numbers are positive.
    prefix = [0]
    for i in range(0, len(nums)):
        prefix.append( prefix[-1] + nums[i])
    # find the min val from the prefix array, minVal + startValue = 1, so startValue = 1 - minVal
    minVal = min(prefix)
    return 1-minVal
nums = [-3,2,-3,4,2]


print(minInitial(nums))


# the code works,but not very fast, need improvement
# def minInitial(nums):
#     if min(nums) >= 0:
#         return 1
    
#     start = 0
#     for num in nums:
#         start += abs(num)
    
    
    
#     while start > 0:
#         print("start is ",start)
#         prefix = [nums[0]+start]
#         for i in range(1, len(nums)):
#             prefix.append( prefix[-1] + nums[i])
#         print('prefix :',prefix)
#         if min(prefix)>1 and start > 1:
#             print("too big")
#             start -= 1
#             continue
#         break
#     return start

# # nums = [-3,2,-3,4,2]
# # nums = [1,-2,-3]
# # nums = [1,2]
# # nums = [2,3,5,-5,-1]
# nums = [-3,2,-3,4,2]


# print(minInitial(nums))


    


    

    
