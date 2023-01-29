class stack:
    def __init__(self,list = None):
        if list == None:
            self.items =[]
        else:
            self.items = list
        self.sizes = 0      
        

    def push(self,data):
        self.items.append(data)
        self.sizes =+ 1

    def pop(self):
        if not self.isEmpty():
            self.sizes =-1
            return self.items.pop()
        else:
            print('Stack is empty')

    def peek(self):
        return self.items[-1]
        #return self.items[len(self.items)-1]

    def isEmpty(self):
        return self.items == []
        return len(self.items) == 0
        return self.size == 0

    def size(self):
        return int(len(self.items))
    
    def __str__(self):
        s = 'stack of ' + str(self.size()) + ' item :\n'
        for ele in self.items:
            s+=str(ele)+'\n'
        return s

s = stack()
s.push('A')
s.push('B')
s.push('C')
print(s.size())
s.pop()

print(s.peek())
print(s.items)
print(s.size())
print(s.isEmpty())

print(s)