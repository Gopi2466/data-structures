
class LinkedList:
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, linkNode):
            self._element = element
            self._next = linkNode
               
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return (self._size)
    
    def isEmpty(self):
        return (self._head is None)
    
    def remove_beg(self):
        if (self.isEmpty()):
            raise Exception("Linked list is empty")
        self._head = self._head._next
        self._size -= 1
    def remove_end(self):
        pass# this is not implemented yet it is a very expensive operation because we have to travel to the position befor the tail.
    
    def insert_end(self, el):
        if (self.isEmpty()):
            self._head = self._Node(el, None)
            self._tail = self._head
        else:
            newest = self._Node(el, None)
            self._tail._next = newest
            self._tail = newest
            self._size += 1
    
    def insert_beg(self, el):     
        self._head = self._Node(el, self._head)
        self._size += 1   
                  

linklist_one = LinkedList()  # this is initializing an empty linked list.


