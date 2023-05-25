# You are given a binary substring s (a string containing only "0" and "1"). An operation involves flipping a "0" into a "1". What is the length of the longest substring containing only "1" after performing at most one operation?

# For example, given s = "1101100111", the answer is 5. If you perform the operation at index 2, the string becomes 1111100111.
def find_length(str):
    ans = left = cnt =  0
    # stack_left = []
    # stack_right = []
    for right in range(len(str)):
        if str[right] == "0":
            cnt += 1
        while cnt > 1:
            if str[left] == '0':
                cnt -= 1
            left += 1
        # stack_left.append(left)
        # stack_right.append(right)
        ans = max(ans, right-left+1)
        
    
    return ans

s = "1101100111"
print(find_length(s))