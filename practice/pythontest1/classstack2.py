class Stack:
    def __init__(self,list= None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def push(self,data):
        self.items.append(int(data))
        
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    '''def pop2(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Empty Stack")
            return -1'''
        
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Empty Stack")
            
s = Stack()
inp = input("Enter num = ").split(",")

for i in inp:
    if i[0]=='A':
        i = i.replace('A','')
        s.push(i)
        
    elif i[0]=='P':
        s.pop()


if s.items == []:
    print('value in stack = empty')
    
else:
    print('value in stack =' ,s.items)        