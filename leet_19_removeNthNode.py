# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#the solution and comment for "if not fast" is from other people. I copied them here for my final understanding.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        #This handles the case where we are deleting the head from the linked list. In that case fast will have traversed the entire linked list. So fast is now null. Then obviously to snip the head, we just return head.next.
        if not fast:
            return head.next
        #below, "while fast" is not being used because we want to get the position of one node in front of the node to be deleted.
        # when fast gets to the last node, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
    
    # "while fast" will make the fast pointer point to null in the end.
    # " while fast.next" will make the fast pointer stop at the last node so that slow pointer will be at the node in front of the node to be deleted.
    