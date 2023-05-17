# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
def occ(arr):
    my_dict = {}
    stack = []
    cnt_stack = []
    for i in range(len(arr)):
        if arr[i] not in stack:
            my_dict[arr[i]] =  1
            print(my_dict)
            stack.append(arr[i])
            print(stack)
        else:
            my_dict[arr[i]] +=  1
            print(my_dict)
    for val in my_dict.values():
        if val not in cnt_stack:
            cnt_stack.append(val)
        else:
            print(f"{val} is repeating")
            return False
    return True
            
print(occ([1,3,1,4,4,4]))