# 2095. Delete the Middle Node of a Linked List
# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        if not head.next:
            return None
        slow = head
        fast = head
        pre = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = slow.next
        return head