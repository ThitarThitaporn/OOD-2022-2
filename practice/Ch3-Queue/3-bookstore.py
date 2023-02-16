class Queue:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if self.size() > 0:
            return self.items.pop()
        else:
            return -1
        
    def size(self):
        return len(self.size())
    
    def isEmpty(self):
        return len(self.items) == 0
    
    