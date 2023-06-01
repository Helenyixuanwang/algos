#  Find Players With Zero or One Losses
# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
#hint: Count the number of times a player loses while iterating through the matches.

from collections import defaultdict

def lose(matches):
    winners = []
    lose_one = []
    counts = defaultdict(int)
    show_up = defaultdict(int)
    
    for i in range(len(matches)):
        for j in range(2):
            if j == 0:
                print("win")
                counts[matches[i][0]] += 1
                show_up[matches[i][0]] += 1
            if j == 1:
                print("lose")
                counts[matches[i][1]] -= 1
                show_up[matches[i][1]] += 1
    print("win lose cnt:",counts)
    print("each one shows up cnt:",show_up)
    for i in counts:
        #if values are equal from both dictionary, then they are all win players
        if counts.get(i) == show_up.get(i):
            winners.append(i)
        #if the difference is 2, then they are lose one players
        if show_up.get(i)-counts.get(i) == 2:
            lose_one.append(i)
    return [sorted(winners), sorted(lose_one)]

matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
print(lose(matches))