# Leet 1394,Find Lucky Integer in an Array. Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

# Return the largest lucky integer in the array. If there is no lucky integer return -1.
from collections import defaultdict
def lucky(arr):
    dict = defaultdict(int)
    ans = -1
    for item in arr:
        dict[item] += 1
    for key,val in dict.items():
        if key == val:
            ans = max(ans,key)

    return ans
# arr = [2,2,3,4]
arr = [1,2,2,3,3,3]

print(lucky(arr))
