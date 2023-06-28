# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Input: nums = [1,2,3,1,1,3]
# Output: 4

#method 3, slow
def good_pairs(nums):
    left = ans = 0
    right = 1
    while left < right:
        for right in range(left+1,len(nums)):
            if nums[left] == nums[right]:
                print("found one :", left,right)
                ans += 1
        left += 1
    return ans
nums = [1,2,3,1,1,3]
print(good_pairs(nums))






#method 1, fast 
from collections import defaultdict
def good_pairs(nums):
    dict = defaultdict(int)
    ans = 0
    for num in nums:
        dict[num] += 1
    for val in dict.values():
        if val > 1:
            ans += val*(val-1)/2
    
    
    return int(ans)
nums = [1,2,3,1,1,3]
print(good_pairs(nums))

# method 2, fast
from collections import Counter
def good_pairs(nums):
    
    ans = 0
    print(Counter(nums))
    for val in Counter(nums).values():
        if val > 1:
            ans += val*(val-1)/2
    
    
    return int(ans)
nums = [1,2,3,1,1,3]
print(good_pairs(nums))