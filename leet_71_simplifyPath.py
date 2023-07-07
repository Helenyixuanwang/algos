# 71. Simplify Path
# Input: path = "/home//foo/"
# Output: "/home/foo"

# Input: path = "/home/"
# Output: "/home"

def simple_path(path):
    stack =[]
    arr = path.split("/")
    print(arr)
    for c in arr:
        if c=="" or c==".":
            continue
        if stack and c == "..":
            stack.pop()
        elif not stack and c=="..":
            continue
        else:
            stack.append(c)
    print("final stack is :",stack)
    return "/"+"/".join(stack)
    
            


# str =  "/home/"
# str ="/home//foo/"
str = "/../"


print(simple_path(str))