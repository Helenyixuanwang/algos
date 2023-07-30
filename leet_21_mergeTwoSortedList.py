# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I learned this from a youtube video
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node to escape edge case
        dummy = ListNode() 
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # if list2 comparison is done and only list1 has nodes left
        if list1:
            tail.next = list1
        # if list1 comparison is done and only list2 has nodes left
        elif list2:
            tail.next = list2

        return dummy.next