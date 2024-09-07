class Queue:
    
    class _Node:
        __slots__ = '_element', '_next'
        def __init__(self, element, linkNode):
            self._element = element
            self._next = linkNode
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def isEmpty(self):
        return (self._head is None)
    
    def __len__(self):
        return (self._size)
    
    def enqueue(self, e):
        
        newest = self._Node(e, None)
        if (self.isEmpty()):
            self._head = newest
            self._tail = self._head
        else:
            self._tail._next = newest
            self._tail = newest
        self._size += 1
        
    def first(self):
        if(self.isEmpty()):
            raise Exception("Queue is empty")
        return self._head._element
    
    def dequeue(self):
        if(self.isEmpty()):
            raise Exception("Queue is Empty")
        else:
            answer = self._head._element
            self._head = self._head._next
            size -= 1
            if self.isEmpty():
                self._tail = None
            return answer