# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]

def running_sum(nums):
    running = [nums[0]]
    
    for i in range(1,len(nums)):
        running.append(nums[i]+ running[-1])
    print(running)
    return running

# nums = [1,2,3,4]
# nums = [1,1,1,1,1]
nums = [3,1,2,10,1]
print(running_sum(nums))