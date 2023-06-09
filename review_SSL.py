##### review singly linked list  #######
class Lnode:
    def __init__(self,val):
        self.val = val
        self.next = None
class Slist:
    def __init__(self):
        self.head = None

    def add_front(self,val):
        new_node = Lnode(val)
        curr_head = self.head
        new_node.next = curr_head
        self.head = new_node
        return self
    
    def add_back(self,val):
        new_node = Lnode(val)
        runner = self.head
        while(runner.next):
            runner = runner.next
        runner.next = new_node
        return self

    def print(self):
        runner = self.head
        while (runner):
            print(runner.val)
            runner = runner.next
        print("#### print done ######")
        return self
    #remove_from_front(self) - remove the first node and return its value
    def remove_front(self):
        if not self.head :
            return None
        val = self.head.val
        self.head = self.head.next
        return val
    #remove_from_back(self) - remove the last node and return its value
    def remove_back(self):
        if not self.head:
            return None
        
        if not self.head.next:
            self.head = None
            return None
        runner = self.head
        while(runner.next.next):
            runner = runner.next
        val = runner.next.val
        runner.next = None
        return val

        
        
    
my_list = Slist()
t_list = Slist()
temp = my_list.add_front(1).add_front(2).add_front(3).add_front(4).remove_back()
my_list.print()
print(temp)
# temp2 = t_list.remove_front()
# print(temp2)

