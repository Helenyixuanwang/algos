# Example 1: 49. Group Anagrams

# Given an array of strings strs, group the anagrams together.

# For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]]

# An anagram is a word or phrase formed by changing the order of the letters in another word or phrase. For example, ' triangle' is an anagram of ' integral'.

# The sorted() function returns a sorted list of the specified iterable object.

# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

from collections import defaultdict
def groupAnagrams( strs):
        groups = defaultdict(list)
        print("groups are like ", groups)
        for s in strs:
            print("s  ",s)
            # to get a key like a string "aet", but not a list like ["a","e","t"]
            key = "".join(sorted(s))
            
            
            print("key is ",key)
            # hash map value part is a list, groups[key] means the value part of hash map
            groups[key].append(s)
        
        return groups.values()
        # return groups

strs= ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))