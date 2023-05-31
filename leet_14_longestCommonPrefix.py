# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
def prefix_str(arr):
    ans = ""
    if len(arr) == 1:
        return ans+arr[0]
    min_str = len(arr[0])
    seen = set()
    
    for i in range(1,len(arr)):
        if len(arr[i]) < min_str:
            min_str = len(arr[i])
            # print("shortest str length is :", min_str)
    for j in range(min_str):
        for i in range(len(arr)):   
            # print("within nested loop") 
            seen.add(arr[i][j])
            print("current seen set is :",seen)
        if len(seen)== 1 :
            print("go if")
            ans += arr[i][j]
            print("ans is :",ans)
            seen.remove(arr[i][j])
            print("after removing, seen is :", seen)
        else:
            # print("go else")
            return ans
        # return ans
    return ans
    

strs = ["flower","flow","flight"]
# strs = ["ab","a"]
# strs = ["a"]
print(prefix_str(strs))