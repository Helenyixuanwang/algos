# duplicate elements, find the first occurence or the left-most element
def binary_search(arr, target):
    left = 0
    right = len(arr)-1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
            # comment out above line, use below line if looking for the last occurence or the right most element
            # left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result

arr = [2,4,10,10,10,18,20]
print(binary_search(arr,10))
    
    