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
    # create counts dictionary, then loop through string order. doesn't care which one is longer
    for i in range(len(order)):
        print("order[i] ",order[i])
        if order[i] in counts:
            print((counts[order[i]]))
            # no for loop is used here, muliplication is easier    
            ans.append(order[i] * counts[order[i]])
            del counts[order[i]]
            print("after deletion ", counts)
    
    # order by key
    for key,val in sorted(counts.items()):
        ans.append(key * val)
    
    return "".join(ans)

# order = "cba"
# s = "abcd"

# order = "cbafg"
# s = "abcd"

order ="kqep"
s ="pekeq"

# order = "hucw"
# s = "utzoampdgkalexslxoqfkdjoczajxtuhqyxvlfatmptqdsochtdzgypsfkgqwbgqbcamdqnqztaqhqanirikahtmalzqjjxtqfnh"
print(custom_sort(order,s))
