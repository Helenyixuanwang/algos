# Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 

def two_sum(s, target):
    i = 0
    j = len(s) - 1
    while (i < j ):
        if (s[i]+s[j]) == target:
            return True
        elif (s[i]+s[j]) > target:
            j -= 1
        elif (s[i]+s[j]) < target:
            i += 1
        
    return False

print(two_sum([1,3,4,5,7,8,11],15))