# Leetcode: 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

def max_ave(nums,k):
    ans = sum = 0.0
    for i in range(k):
        sum += nums[i]
    ans = sum/k
    print(ans)

    for i in range(k,len(nums)):
        sum += nums[i]-nums[i-k]
        avg1 = sum/k
        ans = max(ans, avg1)
        print("avg1:  ",avg1)
        print("ans  :", ans)
    return ans

nums = [1,12,-5,-6,50,3]
k =4
print(max_ave(nums,k))

