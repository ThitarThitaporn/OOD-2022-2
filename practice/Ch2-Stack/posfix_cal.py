
def postfix_cal(exp,is_postfix= False):
    if not is_postfix :
        postfix = exp
    else:
        postfix = exp
    
    s = Stack()
    for i in postfix:
        if i in '01234567889':
            s.push(int(i))
        else:
            a = s.pop()
            b = s.pop()
            if i == '+':
                s.push(b+a)
            elif i == '-':
                s.push(b-a)
            elif i == '*':
                s.push(b*a)
            elif i == '/':
                s.push(b*a)
                
    return s.pop()
------------
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
        #self.size = len(self0.items)-1
        self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
def infix2postfix(exp):
    s = Stack()