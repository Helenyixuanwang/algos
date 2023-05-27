# Leetcode 268: Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2

def missing_num(arr):
    n = len(arr)
    nums = set(arr)
    for i in range(n+1):
        if i not in nums:
            return i
    
# arr1 = [3,0,1]
# arr1 = [0,1]
arr1 =[9,6,4,2,3,5,7,0,1]

print(missing_num(arr1))