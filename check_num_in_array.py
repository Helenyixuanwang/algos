from collections import defaultdict
def  find_num(arr, target):
    
    
    # method 3 binary search tree
    left = 0
    right= len(arr)-1
    while left <= right:
        mid = (right + left)//2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1
    return -1

    # method 1, iterrative
    # for i in range(len(arr)):
    #     if arr[i] == target:
    #         return i
        
    # return -1

    #method 2, hashmap
    # dict = defaultdict(int)
    
    # for i in range(len(arr)):
    #     dict[arr[i]] = i
    # print(dict)
    # for item in dict.keys():
    #     if item == target:
    #         return dict[item]
    # return -1


arr = [2,6,13,21,36,47,63,81,97]
target = 63
print(find_num(arr, target))


# method 4, recurssion
def find_num_recu(arr, left, right, target):
    
    mid = (left + right)//2
    if left > right:
        return -1
    if arr[mid] == target:
        return mid
    if arr[mid] < target:
        return find_num_recu(arr,mid+1,right, target)
    if arr[mid] > target:
        return find_num_recu(arr,left,mid-1, target)

arr = [2,6,13,21,36,47,63,81,97]
print(find_num_recu(arr,0, len(arr)-1, 97))

    