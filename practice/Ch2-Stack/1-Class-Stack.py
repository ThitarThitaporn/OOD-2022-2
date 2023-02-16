class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,data):
        self.items.append(data)
        
    def pop(self ):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Empty Stack")
            return -1
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Empty Stack")
            
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
        