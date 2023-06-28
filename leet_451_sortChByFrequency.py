# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

# Return the sorted string. If there are multiple answers, return any of them.

# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# method 1
from collections import defaultdict
def sort_fre(str):

    dict = defaultdict(int)
    for letter in str:
        dict[letter] += 1
    print(dict)
    print((dict.items()))
    ans = ''
    # print("sorted is like :",sorted(dict, key=lambda item: dict[item],reverse=True))
    for c in sorted(dict, key=lambda item: dict[item],reverse=True):
        #     print("c, dict[c]: ", c, dict[c])
        ans+=c*dict[c]
    return ans

# method 2
from collections import defaultdict
def sort_fre(str):
    dict = defaultdict(int)
    for letter in str:
        dict[letter] += 1
    # print(dict)
    print((dict.items())) # print a list of tuples
    ans = ''
    
    print("sorted is like :",sorted(dict.items(), key=lambda item: item[1],reverse=True))
    # sort per value instead of key, using key=lambda
    for key,val in sorted(dict.items(), key=lambda item: item[1],reverse=True):
        print("key,val: ", key, val)
        ans += key*val
    return ans  

str = "trsuu"
print(sort_fre(str))

## Say we have a list of strings we want to sort by the last letter of the string.
# strs = ['xc', 'zb', 'yd' ,'wa']

#   ## Write a little function that takes a string, and returns its last letter.
#   ## This will be the key function (takes in 1 value, returns 1 value).
# def MyFn(s):
#     return s[-1]

#   ## Now pass key=MyFn to sorted() to sort by the last letter:
# # print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']
# print(sorted(strs, key=len))  

# student_tuples = [
#     ('john', 'A', 15),
#     ('jane', 'B', 12),
#     ('dave', 'B', 10),
# ]
# print(sorted(student_tuples, key=lambda student: student[0]))  # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

#sort by key
print(sorted(people))
#[1, 2, 3, 4], only return a list of keys, not values

#sort by key
print(sorted(people.items()))
#[(1, 'Jill'), (2, 'Jack'), (3, 'Jim'), (4, 'Jane')], sort per key, but also display value in list of tuples

#sort by value
print(sorted(people.items(), key=lambda item: item[1]))
#[(2, 'Jack'), (4, 'Jane'), (1, 'Jill'), (3, 'Jim')]

# Sort by key
print(dict(sorted(people.items())))
# {1: 'Jill', 2: 'Jack', 3: 'Jim', 4: 'Jane'}, sort per key, also display value in dictionary

# Sort by value
print(dict(sorted(people.items(), key=lambda item: item[1])))
#{2: 'Jack', 4: 'Jane', 1: 'Jill', 3: 'Jim'}

print(sorted(people, key=lambda item: people[item]))
    
    
people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}
print(people.items())
#dict_items([(3, 'Jim'), (2, 'Jack'), (4, 'Jane'), (1, 'Jill')])
print(people.keys())
#dict_keys([3, 2, 4, 1])
print(people.values())
#dict_values(['Jim', 'Jack', 'Jane', 'Jill'])

str = "u"
print(9*str)