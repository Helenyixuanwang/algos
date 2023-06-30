# 1436. Destination City
# Input: paths = [["B","C"],["D","B"],["C","A"]]
# Output: "A"

def destination(paths):
    ans = ""
    starting = []
    ending= []
    for i in range(len(paths)):
        starting.append(paths[i][0])
        ending.append(paths[i][1])
    for city in ending:
        if city not in starting:
            ans += city
    return ans
# paths = [["B","C"],["D","B"],["C","A"]]
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

print(destination(paths))
