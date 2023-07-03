# 290. Word Pattern
# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

def word_pattern(pattern,s):
    arr = s.split()
    # use of hash map
    dict = {}
    dict2 = {}
    if len(pattern) != len(arr): # edge case for test case 3
        return False
    for i in range(len(pattern)):
        if (pattern[i] in dict and arr[i] != dict[pattern[i]]) or (arr[i] in dict2 and pattern[i]!= dict2[arr[i]]):
            # print("pattern[i]  arr[i]  dict[pattern[i]]", pattern[i],arr[i], dict[pattern[i]])
            print(dict)
            print(dict2)
            return False
        dict[pattern[i]] = arr[i]
        dict2[arr[i]] = pattern[i]
    print(dict)
    return True

# **** test case 1 *****
# s = "dog cat cat fish"
# s = "dog cat cat dog"
# s = "dog dog dog dog"
# pattern = "abba"

# **** test case 2 ******
# pattern = "aaaa"
# s = "dog cat cat dog"

# **** test case 3 ****
pattern ="aaa"
s = "aa aa aa aa"
print(word_pattern(pattern ,s))

