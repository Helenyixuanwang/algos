#  Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.
#Leetcode 3
from collections import defaultdict

def longest_subStr_unique(str):
    dict = defaultdict(int)
    ans = left = 0
    
    for right in range(len(str)):
            # print(dict)
            dict[str[right]] += 1
            while 2 in dict.values():
                print("2 exists: ")
                dict[str[left]] -= 1
                if dict[str[left]] == 0:
                    del dict[str[left]]
                print(dict)
                left += 1
                
                print("left, right:", left, right)
            print("final dict:",dict)
            ans = max(ans, right-left+1)
            print("ans:",ans)
    return ans




# str1 = "pwwkew"
str1 = "abcabcbb"    
print(longest_subStr_unique(str1))    

        
        
        
