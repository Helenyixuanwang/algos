# 791. Custom Sort String
# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.


# Input: order = "cba", s = "abcd"
# Output: "cbad"

# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
from collections import Counter
def custom_sort(order,s):
    ans = []
    counts = Counter(s)
    print(counts)
    
    if len(order) <= len(s):
        for i in range(len(order)):
            print("order[i] ",order[i])
            if order[i] in counts:
                print((counts[order[i]]))
                for _ in range(counts[order[i]]):
                    ans.append(order[i])
                    print("within for loop, appending ",order[i])
                del counts[order[i]]
                print("after deletion ", counts)
                print("current ans is ",ans)

            else:
                continue
    if len(order) > len(s):
        for i in range(len(s)):
            if order[i] in s:
                print(counts[order[i]])
                for _ in range(counts[order[i]]):

                    ans.append(order[i])
                
                    del counts[order[i]]

            else:
                continue

    if counts.keys():
        temp = sorted(counts.keys())
        print("extra letters are ",temp)
        # print((counts.keys()))
        for i in range(len(temp)):
            print(temp[i])
            for _ in range(counts[temp[i]]):
                print("appending ...", temp[i])
                ans.append(temp[i])
    return "".join(ans)

# order = "cba"
# s = "abcd"

# order = "cbafg"
# s = "abcd"

# order ="kqep"
# s ="pekeq"

order = "hucw"
s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
print(custom_sort(order,s))
