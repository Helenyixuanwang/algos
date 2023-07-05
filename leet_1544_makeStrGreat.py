# 1544. Make The String Great
# Given a string s of lower and upper case English letters.

# A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

# 0 <= i <= s.length - 2
# s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
# Input: s = "leEeetcode"
# Output: "leetcode"

def make_str_great(s):
    stack = []
    for i in range(len(s)):
        
        if stack and (s[i] != stack[-1]) and (s[i].lower() == stack[-1].lower()):
            stack.pop()
            print("after pop, stack is ",stack)
        else:
            stack.append(s[i])
            print("after appending, stack is ", stack)
    if not stack:
        return ""
    return "".join(stack)
    
# s = "abBAcC"    
# s = "leEeetcode"
s = "s"
print(make_str_great(s))
    

