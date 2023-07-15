# this is sth I have learned from a youtube video. It is fun and very import to know.
import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_value = collections.OrderedDict()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        check = self.key_value.get(key, None)
        if check:
            self.key_value.move_to_end(key)
            return check
        else:
            return -1        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        check = self.key_value.get(key, None)
        if check:
           self.key_value.move_to_end(key)
        self.key_value[key] = value

        if len(self.key_value) > self.capacity:
            # pop the oldest one in the queue
            self.key_value.popitem(last = False)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)