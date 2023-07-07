# 71. Simplify Path
# Input: path = "/home//foo/"
# Output: "/home/foo"

# Input: path = "/home/"
# Output: "/home"

def simple_path(str):
    stack =[]
    arr = str.split("/")
    for c in arr:
        if c=="" or c==".":
            continue
        if stack and c == "..":
            stack.pop()
        else:
            stack.append(c)
    print("final stack is :",stack)
    return "/"+"/".join(stack)
    
            

 
str =  "/home/"
# str ="/home//foo/"

print(simple_path(str))