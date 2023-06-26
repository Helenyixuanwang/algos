# Leetcode 209, Minimum Size Subarray Sum
#Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
# this is practice I did by myself

def minSubArrayLen( target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = right= 0
        ans = float('inf')
        
        curr = 0
        for right in range(len(nums)):

            curr += nums[right]
            print("curr is ", curr)
            # once the current sum satisfies ">= target", can memorize the window size,
            # since we are seeking the minimal window size, once it is >= window size, we can 
            # shrink the size next step, until it satisfies the condition again.
            while curr >= target:
                ans = min(ans, right - left + 1)
                print("current ans is ",ans)
                curr -= nums[left]
                left += 1
            
            
        if ans <  float('inf'):   
            return ans
        else:
            return 0

# Input: target = 7, nums = [2,3,1,2,4,3]
target = 7
nums = [2,3,1,2,4,3]
# Output: 2
print(minSubArrayLen(target, nums))