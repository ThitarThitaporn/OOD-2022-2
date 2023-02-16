class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items =[]
        else:
            self.items = list
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

e = input('Enter expresion : ')

def match(open, close):
    return (open == '(' and close == ')') or (open == '{' and close == '}') or (open == '[' and close == ']')

def parenMathching(str):
    s = Stack()
    i = 0
    error = 0
    c = 0

    while i < len(str) and error ==0:
        c = str[i]
        if c in '{[(':
            s.push(c)
        else:
            if c in '}])':
                if s.size() > 0:
                    if not match(s.pop(), c):
                        error = 1
                else:
                    error = 2
        i += 1
    
    if s.size() > 0 and error == 0:
        error = 3
    
    return error, c, i, s

err, c, i, s = parenMathching(e)
if err == 1:
    print(e, 'Unmatch open-close')
elif err == 2:
    print(e, 'close paren excess')
elif err == 3:
    print(e, 'open paren excess  ', s.size(), ': ', end = '')
    for ele in s.items:
        print(ele, sep = '', end = '')
else:
    print(e, 'MATCH')