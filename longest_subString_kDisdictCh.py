# Example 1: You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
from collections import defaultdict
def longest(str, k):
    left = ans = 0
    dict = defaultdict(int)
    for right in range(len(str)):
        print(dict)
        dict[str[right]] += 1
        print(dict)
        while len(dict) > 2:
            dict[str[left]] -= 1
            print(dict)
            if dict[str[left]] == 0:
                del dict[str[left]]
            left += 1
            print(dict)
        
        ans = max(ans, right-left +1)
    return ans

str = "eceba"
k =2 
print(longest(str,k))

# this is an example from crash course