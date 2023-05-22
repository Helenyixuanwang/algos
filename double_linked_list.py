#  to implement a doubly linked list 1 <-> 2 <-> 3.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
    
# Write your code here
# Try creating 1 <-> 2 <-> 3
# Test with print()


head = ListNode(None)
tail = ListNode(None)



one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
head.next = one
one.prev = head
one.next = two
two.prev = one
two.next = three
three.prev = two
three.next = tail
tail.prev = three
dummy = head
while dummy:
        print(dummy.val)
        dummy = dummy.next
