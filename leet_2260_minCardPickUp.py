#  2260. Minimum Consecutive Cards to Pick Up

# Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
# want to use slide window to do it again
# the duplicate element seem to appear only once in the example code, not sure if the same element shows up more than twice
# this code is copied from course platform

from collections import defaultdict
def minimumCardPickup( cards):
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
        print(dic)   
        ans = float("inf")
        
        for key in dic:
            arr = dic[key]
            print(arr)
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
        
        return ans if ans < float("inf") else -1

cards = [1, 2, 6, 2, 1]

print(minimumCardPickup(cards))