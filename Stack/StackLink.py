class Stack:
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, linkNode):
            self._element = element
            self._next = linkNode
            
    def __init__(self):
        self._head = None
        self._size = 0
        
    def __len__(self):
        return (self._size)
    
    def isEmpty(self):
        return self._head is None
    
    def push(self, e):
        if (self.isEmpty()):
            self._head = self._Node(e, None)
            
        else:
            self._head = self._Node(e, self._head)
            
        self._size += 1
    
    def pop(self,e):
        if (self.isEmpty()):
            raise Exception("Stack is empty")
        else:
            answer = self._head._element
            self._head = self._head._next
            self.size -= 1
            return answer
        
    
    def top(self):
        # this will return but not remove the element.
        if(self.isEmpty()):
            raise Exception("Stack is empty")
        else:
            return self._head._element