#Leetcode 9
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise

# Input: x = 121
# Input: x = -121

def panlindrom_int(x):
    #make it into a int list
    int_arr = str(x)
    print(int_arr)
    left = 0
    right = len(int_arr)-1
    while left <= right:
        if int_arr[left] != int_arr[right]:
            return False
        left += 1
        right -= 1
    return True

# x = 121
# x= -121
x=10
print(panlindrom_int(x))