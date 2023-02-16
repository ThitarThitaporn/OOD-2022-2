class Stack:
    def __init__(self,list = []):
        if list == None:
            self.items = []
        else:
            self.items = list
        
    def size(self):
        return len(self.items)   
     
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return -1
        
    
            
def match(op,cl):
    return (op == '('and cl ==')') or (op == '{'and cl=='}') or (op == '['and cl==']')

def parenMatching(str):
    s = Stack()
    i = 0
    error = 0
    c = 0
    
    while i < len(str) and error == 0:
        c = str[i]
        if c in '{[(':
            s.push(c)
            
        else:
            if c in ')]}':
                if s.size()>0:
                    if not match(s.pop(),c):
                        error = 1
                else:
                    error = 2
                    
        i += 1
    
    if s.size()>0 and error == 0 :
        error = 3
    
    return error,c,i,s
    
exp = input("Enter expresion : ")
err,c,i,s = parenMatching(exp)
if err == 1:
    print(f"{exp} Unmatch open-close")
elif err == 2:
    print(f"{exp} close paren excess")
elif err == 3:
    print(f"{exp} open paren excess   {s.size()} : ",end='')
    for ele in s.items:
        print(ele, sep ='' ,end ='')

else:
    print(f'{exp} MATCH')
    
    
        