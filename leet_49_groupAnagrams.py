# Example 1: 49. Group Anagrams

# Given an array of strings strs, group the anagrams together.

# For example, given strs = ["eat","tea","tan","ate","nat","bat"], return [["bat"],["nat","tan"],["ate","eat","tea"]]

# An anagram is a word or phrase formed by changing the order of the letters in another word or phrase. For example, ' triangle' is an anagram of ' integral'.


from collections import defaultdict
def groupAnagrams( strs):
        groups = defaultdict(list)
        print("groups are like ", groups)
        for s in strs:
            print("s  ",s)
            # to get a key like a word "aet", but not "a","e","t"
            key = "".join(sorted(s))
            
            
            print("key is ",key)
            # hash map value part is a list, groups[key] means the value part of hash map
            groups[key].append(s)
        
        return groups.values()
        # return groups

strs= ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))