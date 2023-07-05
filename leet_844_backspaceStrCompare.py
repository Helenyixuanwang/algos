# Example 3: 844. Backspace String Compare

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# For example, given s = "ab#c" and t = "ad#c", return true. Because of the backspace, the strings are both equal to "ac".


# When I review this algo, I was able to write it and make it work. I just reppeatedly write same block of code twice to iterate through string s and t. When I read the sample code from the platform, I notice that a function could be created so that I do not have to repeat myself. Cool!

def backspace_string(s,t):
    def build(str):
        stack = []
        for c in str:
            if c == "#":
                stack.pop()
            else:
                stack.append(c)
        print(stack)
        return "".join(stack)
    return build(s) == build(t)

s = "ab#c"
t = "ad#c"

print(backspace_string(s,t))