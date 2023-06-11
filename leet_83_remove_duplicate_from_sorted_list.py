def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        
        
        if head:
            back = head
            front = back.next
        else:
            return head
        
        while back and front:
            if back.val == front.val:
                back.next = front.next
                front = front.next
            else:
                back = front
                front = front.next
        return head


#solution 2, accepted by Leetcode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
    
        
        
        if not head:
            return None
        ptr = head
        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
            else: 
                ptr = ptr.next
        return head
      
      