#  Squares of a Sorted Array
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

def squares_sort(arr):
    #left, right pointer of arr
    l = 0
    r= len(arr)-1
    #pointer of newArr
    ptr = r
    #initialization of newArr
    newArr = [0] * len(arr)
    
    print(newArr)
    while l >=0 and r < len(arr) and r >= l:
        if abs(arr[l])> abs(arr[r]):
            print("left, right \n", arr[l],arr[r])
            print("left big")
            print(arr[l]*arr[l])
            newArr[ptr] = arr[l]*arr[l]
            ptr -= 1
            print(newArr[r])
            
            l +=1

        else:
            print("right big")
            newArr[ptr]=arr[r]*arr[r]
            ptr -= 1
            r -= 1
    return newArr
print(squares_sort([-11,-3,-1,1,3,10]))