class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[-1]
    
def infix2postfix(exp):
    S = Stack()
    operator = "+-*/"
    priority = {'+':0, '-':0, '*':1, '/':1}
    result = ''

    for ele in exp:
        if ele in '+-*/^':
            if S.isEmpty():
                S.push(ele)
            else:
                while not S.isEmpty():
                    if S.peek() == '(':
                        break
                    else:
                        if priority.get(S.peek()) >= priority.get(ele):
                            result += str(S.pop())
                        else:
                            break
                S.push(ele)
        elif ele == '(':
            S.push(ele)
        elif ele == ')':
            while S.peek() != '(':
                result += str(S.pop())
            S.pop()
        else:
            result += str(ele)

    print(result, end='')

    while not S.isEmpty():
        print(S.pop(), end='')

    
           
    
    
    
    
print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

infix2postfix(token)