# 2260. Minimum Consecutive Cards to Pick Up
# Given an integer array cards, find the length of the shortest subarray that contains at least one duplicate. If the array has no duplicates, return -1.
#   from crash course originally"

from collections import defaultdict
def minimumCardPickup(cards) :
        dic = defaultdict(list)
        for i in range(len(cards)):
            dic[cards[i]].append(i)
        print("dic is ", dic)
        ans = float("inf")
        print("initial value of ans is :",ans)
        for key in dic:
            arr = dic[key]
            print("arr is :",arr)
            for i in range(len(arr) - 1):
                ans = min(ans, arr[i + 1] - arr[i] + 1)
                print("this turn, ans is ",)
        
        return ans if ans < float("inf") else -1

cards = [1, 2, 6, 2, 1]
print(minimumCardPickup(cards))