# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.
#leetcode 1426
def counting_element(arr):
    arrSet = set(arr)
    print(arrSet)
    ans = 0
    for num in arr:
        if (num + 1) in arrSet:
            ans += 1       
    return ans
    
    # return cnt

# arr = [1,2,3]
arr = [1,1,3,3,5,5,7,7]
# arr = [1, 1, 2,2,3,3,5,5,7,7]
print(counting_element(arr))