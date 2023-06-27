# 1748. Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

#  Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
from collections import defaultdict
def sumOfUnique(arr):
    dict = defaultdict(int)
    sum = 0
    for item in arr:
        dict[item] += 1

    for key,val in dict.items():
        if val == 1:
            sum += key
    return sum
nums = [1,2,3,2]

print(sumOfUnique(nums))

