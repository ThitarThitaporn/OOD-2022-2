class Stack:
    def __init__(self,list=[]):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = 0
        
    def push(self,data):
        self.items.append(int(data))
        self.size = len(self.items)
    
    def pop(self):
        self.pop()