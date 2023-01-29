class Stack:
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
def parenMatch(listEX):
     
    S1 = Stack()
    for ele in listEX:
        if ele in '({[' :
            S1.push(ele)
        elif ele in ')}]':
            if S1 is not S1.isEmpty():
                ch = S1.pop()
                if '({['.index(ch)!= ' )}]'.index(ele):
                    return False
                    
            else:
                return False #close ex
    if S1.isEmpty():
        return True
    return False
    return 0
    
Ex="(x+b)*{z/x}/[s+10]"
print(parenMatch(Ex))