# 2390. Removing Stars From a String
# You are given a string s, which contains stars *.

# In one operation, you can:

# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.
# Input: s = "leet**cod*e"
# Output: "lecoe"

def remove_stars(s):
    stack = []
    for c in s:
        if stack and c == "*":
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)

# s = "leet**cod*e"
s = "erase*****"

print(remove_stars(s))