class stack:
    def __init__(self,list = None):
        if list == None:
            self.items =[]
        else:
            self.items = list
      
        

    def push(self,i):
        self.items.append(i)
        self.size =+ 1

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return int(len(self.items))

s = stack()
print(s.items)
print(s.size())