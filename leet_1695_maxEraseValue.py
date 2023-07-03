# 1695. Maximum Erasure Value
# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].
from collections import defaultdict
def max_erase(nums):
    dict = defaultdict(int)
    ans,left = 0,0
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    print(prefix)
    for right in range(len(nums)):
        dict[nums[right]] += 1
        print("adding from right ",dict)
        while dict[nums[right]] == 2:
            print("There are values greater than 2 ",dict)
            dict[nums[left]] -= 1
            if dict[nums[left]] == 0:
                del dict[nums[left]]
            left += 1
        ans = max(ans, prefix[right]-prefix[left]+nums[left])
    return ans

# nums = [4,2,4,5,6]
nums = [5,2,1,2,5,2,1,2,5]
print(max_erase(nums))