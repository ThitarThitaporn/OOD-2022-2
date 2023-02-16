class Stack:
    def __init__(self,list =[]):
        if list == None:
            self.items = []
        else:
            self.items = list
        self.size = 0
        
    def push(self,data):
        self.items.append(int(data))
        self.size = len(self.items)
        print( f'Add = {data} and Size = {self.size}')
    
    def pop(self):
        self.size = len(self.items)-(1)
        if self.items == []:
            print('-1')
            return -1
        else:
            print(f"Pop = {self.items[-1]} and Index = {self.size}")
        self.items.pop()
     
S = Stack()
inp = input("Enter Input : ").split(',')
for i in inp:
    if (i[0] == 'A'):
        i = i.replace('A ','')
        S.push(i)
    elif (i[0] == 'P'):
        S.pop()

if S.items == []:
    print('Value in Stack = Empty')
else :
    print('Value in Stack =' ,*S.items)