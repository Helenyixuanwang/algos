# Maximum Number of Balloons

# Input: text = "loonbalxballpoon"
# Output: 2
from collections import defaultdict

#### this is my code. It works ,but way too long. I like the way another person uses as below 
# def balloon(str):
#     temp_set = set("balloon")
#     balloon_arr = []
#     counts = defaultdict(int)
#     ans = len("balloon")
#     flag = 0
#     print(temp_set)
#     for c in str:
#         balloon_arr.append(c)
#     print("balloon array :",balloon_arr)
#     for c in range(len(balloon_arr)):
#         counts[balloon_arr[c]] += 1
#     print("all values:",counts.values())
#     for val in counts.values():
#         ans = min(val,ans)
#     # print("shortest value is :",ans)
#     print("counts before subtraction:", counts)
#     while counts["a"] >0 and counts["b"] >0 and counts["l"]//2 >=1 and counts["n"]>0 and counts["o"]//2>=1:
#         counts["a"] -= 1
        
#         counts["b"] -= 1
        
#         counts["o"] -= 2
        
#         counts["l"] -= 2
        
#         counts["n"] -= 1
#         print("one balloon created")
#         flag +=1
#     return flag

#the is the copy from another person, so fast and clear
def balloon(text):
        counts = defaultdict(int)
        tSet = set('balloon')
        for c in text:
            if c in tSet:
                counts[c] += 1
        print("print counts before divide 2:", counts)
        #there are two "l" and two "o" in "balloon", so divided by 2. If there are triple letters, 
        #may divided by 3, etc.
        counts['l'] //= 2
        counts['o'] //= 2
        print("print counts after division:", counts)
        print("print tSet:", tSet)
        print("counts and tset length", len(counts), len(tSet))
        if len(counts) == len(tSet):
            return min(counts.values())
        else:
            return 0
        

        
# text = "loonbalxballpoon"
# text =  "nlaebolko"
# text =  "balon"
text = "balllllllllllloooooooooon"
print(balloon(text))

