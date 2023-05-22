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
      