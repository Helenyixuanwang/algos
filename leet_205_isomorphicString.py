# 205. Isomorphic Strings
# Input: s = "egg", t = "add"
# Output: true

# Input: s = "foo", t = "bar"
# Output: False

# Input: s = "paper", t = "title"
# Output: true

# I learn to solve this after watching a solution video. so cool!


def isomorphic(s,t):
    dict1, dict2 = {},{}

    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        if (c1 in dict1 and dict1[c1] != c2) or (c2 in dict2 and dict2[c2] != c1):
            return False
        dict1[c1] = c2
        dict2[c2] = c1 
    return True

    

# s= "paper"
# t = "title"
# s= "foo"
# t="bar"
s = "bbbaaaba"
t = "aaabbbba"

print(isomorphic(s,t))

