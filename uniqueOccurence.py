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

#method 2, make use of set
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
    #make the values into a set, if duplicates exist, it will be ignored according to the set definition        
    this_set = set((my_dict.values()))
    print(this_set)
    # length of this_set will be shorter if duplicates exist, then it is not unique, return False
    if len(this_set) < len(my_dict.values()):
        print("duplicated occurance exists")
        return False
    else:
        print("Unique")
        return True
print(occ([1,3,1,4,4,]))


#method 3, make use of defaultdict
from collections import defaultdict 

def unique_occ(arr):
    dict = defaultdict(int)
    for num in arr:
        dict[num] += 1
        print(dict)
    val_set = set(dict.values())
    print(val_set)
    return len(val_set)==len(dict)

arr1 = [1,3,1,3,4,4]
print(unique_occ(arr1))
# print(unique_occ([1,3,2,14,4,]))
