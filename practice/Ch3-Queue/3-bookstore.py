class Queue:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if len(self.items) == 0:
            return None
        
        return self.items.pop(0)
        
  
    
inp = input("Enter Input : ").split("/")
inp1 = inp[0]
inp2 = inp[1].split(',')

book = Queue(inp1.split(' '))
for i in inp2 :
    if i == 'D':
        book.dequeue()
    else:
        e = i.split(" ")[1]
        book.enqueue(e)
        
        
seen = {}
check = book.items
isDup = False
for c in check:
    if c in seen:
        isDup = True
        break
    else:
        seen[c] = 1
    
if not isDup:
    print('NO Duplicate')
else:
    print('Duplicate') 
    