def two_sum(arr, target):
    dic = {}
    for i in range(len(arr)):
        num = arr[i]
        complement = target - num
        if complement in dic:
            return[i, dic[complement]]
        dic[num] = i
    return [-1,-1]

arr1 = [5,2,7,10,3,9]
print(two_sum(arr1,12))
