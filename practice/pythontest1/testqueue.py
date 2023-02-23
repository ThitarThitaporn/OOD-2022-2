class Queue:
    def __init__ (self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
q = Queue()
inp = input('Enter Input').split(',')

for i in inp:
    if i[0] == 'E':
        print(f'Add {i[2:]} inndex is {q.size()}')
        
        q.enqueue(i[2:])
    
    else:
        x = q.dequeue()
        if x == -1:
            print(x)
        else:
            print(f'Pop {x} size in queue is {q.size()}')
            
if q.isEmpty():
    print('empty')
    
else:
    print(f'numbet in queue : {q.items}')
