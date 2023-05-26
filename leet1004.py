# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
#leetcode 1004

def max_arr_flipK(nums,k):
    left = cnt = ans = 0
    print("k is ", k)
    for right in range(len(nums)):
        # print("in for loop now...")
        if nums[right] == 0:
            print(" found a zero...")
            cnt += 1
            print("cnt is :",cnt)
        while cnt > k:
            if nums[left]==0:
                cnt -= 1
                print(f"slide the window, remove zero at index[{left}], cnt becomes {cnt}")
            left += 1
        print("left, right", left, right)
        ans = max(ans, right-left+1)
    return ans

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

print(max_arr_flipK(nums,k))
    