# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# from collections import Counter
# from collections import defaultdict
# method 1, faster
def containsDuplicate(nums):
    # if len(set(Counter(nums).values())) == 1 and min(Counter(nums).values())==1:
    #     print(set(Counter(nums).values()))
    #     return False
    # else:
    #     return True
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# method 2
from collections import defaultdict
def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
    
        if max(dict.values()) > 1:
            
            return True
        else:
            return False

# method 3,
from collections import defaultdict
def containsDuplicate( nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
        
            if dict[num] > 1:
                return True
        
        return False

# method 4,
from collections import Counter
def containsDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(Counter(nums).values())) == 1 and min(Counter(nums).values())==1:
            print(set(Counter(nums).values()))
            return False
        else:
            return True


# nums = [1,2,3,1]
nums = [1,2,3,4,4]
# nums = [0,4,5,0,3,6]
# nums = [7,10,5,5,6,6,4,10,5,4,9,4,9,6,5,9,6,3,6,5,6,7,7,4,9,9,10,5,8,1,8,3,2,7,5,10,1,8,5,8,4,3,6,4,9,4,2,8,3,2,2,1,5,6,3,2,6,1,8,6,2,9,1,4,5,10,8,5,10,5,10,1,4,8,3,6,4,10,9,1,1,1,2,2,9,6,6,8,1,9,2,5,5,2,1,8,5,2,3,10]
print(containsDuplicate(nums))
