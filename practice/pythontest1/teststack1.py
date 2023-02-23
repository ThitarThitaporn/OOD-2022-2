class Stack:
    def __init__(self,list=None):
        if list == None:
            self.items = []
            
        else:
            self.items = list
            
    def push(self,data):
        self.items.append(data)
        self.size = len(self.items)
        print(f'Add = {data} and size = {self.size}')
        
    def pop(self):
        self.size = len(self.items)-(1)
        if self.items == []:
            print('-1')
            return -1
        else:
            print(f'Pop =  {self.items[-1]} and Index = {self.size}')
            
        self.items.pop()
        
s = Stack()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i[0] == 'A':
        i = i.replace('A','')
        s.push(i)
        
    elif i[0] == 'P':
        s.pop()
        
if s.items == []:
    print('stck is empty')
else:
    print('value in stack is ',*s.items)