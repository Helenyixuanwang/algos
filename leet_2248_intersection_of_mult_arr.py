# Example 2: 2248. Intersection of Multiple Arrays

# Given a 2D array nums that contains n arrays of distinct integers, return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
#this is a review practice after the first time reading from the crash course, 
# the idea is still the same as original one, but the style is slightly different
from collections import defaultdict
def intersection_arr(arr):
    times = len(arr)
    ans = []
    dict = defaultdict(int)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            dict[arr[i][j]] += 1
            
    print(dict)
    for key in dict:
        if dict[key] == times:
            ans.append(key)
    return ans

arr =  [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]

intersection_arr(arr)
print(intersection_arr(arr))
        
