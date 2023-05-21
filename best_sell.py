#Leetcode 121, copy from a solution, not created by myself.


def best_sell(prices):
    l = 0
    r = 1
    maxV= 0
    while r < len(prices):
        current = prices[r] - prices[l]
        if prices[r] > prices[l]:
            maxV = max(maxV, current)
        else:
            l = r
        r += 1
    return maxV

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# prices = [2,4,1]
print(best_sell(prices))






