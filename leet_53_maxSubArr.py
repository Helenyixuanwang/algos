# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

def maxSum_subArr(arr):
    maxSum = arr[0]
    curSum = 0
    for n in arr:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSum = max(maxSum, curSum)
    return maxSum

arr = [-2,1,-3,4,-1,2,1,-5,4]
# arr = [2,1,3,4,1,2,1,5,4]
print(sum(arr))
print(maxSum_subArr(arr))