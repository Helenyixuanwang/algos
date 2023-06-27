#Leet 771 Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Input: jewels = "z", stones = "ZZ"
# Output: 0

def jewels_stones(jewels, stones):
    counts = 0
    for c in stones:
        if c in jewels:
            counts += 1
    return counts

# jewels = "aA"
# stones = "aAAbbbb"

jewels = "z"
stones = "ZZ"

print(jewels_stones(jewels, stones))
