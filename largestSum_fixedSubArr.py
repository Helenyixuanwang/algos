# Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
# // first approach
# function fn(arr, k):
#     curr = some data type to track the window

#     // build the first window
#     for i in [0, k - 1]:
#         Do something with curr or other variables to build first window

#     ans = answer variable, might be equal to curr here depending on the problem
#     for i in [k, arr.length - 1]:
#         Add arr[i] to window
#         Remove arr[i - k] from window
#         Update ans

#     return ans

def fixArr_largeSum(nums, k):
    sum = 0
    #build the first Window 
    for i in range(0, k):
        sum += nums[i]
    print(sum)
    ans = sum
    for i in range(k, len(nums)):
        sum += nums[i]
        sum -= nums[i-k]
        large_sum = max(ans, sum )
    return large_sum

arr1= [3,-1,4,12,-8,5,6]

print(fixArr_largeSum(arr1,4))
