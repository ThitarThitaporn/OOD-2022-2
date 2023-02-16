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

def infix_to_postfix(exp):
    ans =''
        #match ค่าpriority
    priority = "(+-*//"
    priorityvalue = "02244"
        
    s = stack()
    for ele in exp:
        if ele in "+-*/":
            if s.isEmpty():
                s.push(ele)
            else:
                '''while not s.isEmpty():
                    if int(priority[priority.index(s.peek())]) > \
                        int(priorityvalue[priority.index(ele)]) :
                            s.push(ele)
                    else:
                        ans = ans + str(s.pop())'''
                while not s.isEmpty():
                        if int(priority[priority.index(s.peek())]) >= \
                            int(priorityvalue[priority.index(ele)]) :
                                ans = ans + str(s.pop())
                            
                        else:
                            break
                        s.push(ele)            
                    
        else:
            ans = ans + str(ele)
        
    while not s.isEmpty():
        ans += ans + str(s.pop())
            
    return ans


exp = "a*b+c"
print(infix_to_postfix(exp))

    