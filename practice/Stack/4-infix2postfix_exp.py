class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,data):
        self.items.append(int(data))
        #self.size = len(self.items)
        
    def pop(self):
        #self.size = len(self.items)-1
        self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
def infix2postfix(exp):
    s = Stack()