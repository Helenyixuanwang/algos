# Example 2: 2270. Number of Ways to Split Array

# Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.

#make use of prefix sum
def numOfSplitArr(nums):
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    print(prefix)

    ans = 0
    for i in range(len(nums) - 1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            print("split at index:",i)
            ans += 1
    return ans

nums = [3,1,-5,6]
print(numOfSplitArr(nums))


