class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
inp = input("Enter Infix : ")
S = Stack()
print('Postfix : ', end='')

operator = "+-*/^"
priority = {'+':0, '-':0, '*':1, '/':1, '^':2}
result = ''

for ele in inp:
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

print()
           
    
    