# Leet 35. Search Insert Position
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
def searchInsert( nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]
            
            if num == target:
                return mid
            
            if num > target:
                right = mid - 1
            else:
                left = mid + 1
        #when exit from the while loop, left will be greater than right and will be the variable we are looking for
        return left

nums = [1,3,5,9]
target = 8
print(searchInsert(nums, target))