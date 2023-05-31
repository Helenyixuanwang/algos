# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].

def count_odd(low, high):
    
    if (low < 0 ) or (high < 0):
        return 0
    if (low % 2) ==1 and (high % 2)==1:
        
        return (high-low+1)//2+1
    else:
        return (high-low+1)//2

print(count_odd(5,7))
