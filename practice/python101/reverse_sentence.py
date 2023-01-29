# creating an empty stack
string = input()
stack = []

for word in string.split():
    stack.append(word)

reversed_words = []
 
while stack:
    reversed_words.append(stack.pop())
    
reversed_string = " ".join(reversed_words)
print(reversed_string)