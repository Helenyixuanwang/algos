#   Minimum Value to Get Positive Step by Step Sum
# Input: nums = [1,-2,-3]
# Output: 5

def min_val_toGetPositive(nums):
    prefix = [nums[0]]
    for i in range(1,len(nums)):
        prefix.append(nums[i] + prefix[-1])
    print(prefix)
    val = min(prefix)
    print(val)
    if val >=1:
        return 1
    else:
        return abs(val)+1

    # for i in range(len(nums)):
    #     temp = prefix[i] + nums

    # return abs(val)+1

# nums = [1,-2,-3]
nums = [1,2]
# nums = [-3,2,-3,4,2]
print(min_val_toGetPositive(nums))