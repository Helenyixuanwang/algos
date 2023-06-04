#from course, not my creation
# Example 2: 1047. Remove All Adjacent Duplicates In String

# You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

# For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.
def removeDuplicates(s) :
        stack = []
        for c in s:
            print(stack)
            if  stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        
        
        return "".join(stack)

s = "abbaca"
print(removeDuplicates(s))