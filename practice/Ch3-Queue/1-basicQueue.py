class Queue:
    def __init__(self,list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
            
    def enqueue(self,data):
        self.items.append(data)
        
    def dequeue(self):
        if self.size() > 0:
            return self.items.pop(0)
        else:
            return -1
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
inp = input("Enter Input : ").split(",")
q = Queue()

for i in inp:
    if i[0] == 'E' :
        print(f'Add {i[2:]} index is {str(q.size())}')
        
        q.enqueue(i[2:])
        
    else:
        x = q.dequeue()
        if x == -1:
            print(x)
        else:
            print(f'Pop {x} size in queue is {str(q.size())}')
            
            
if q.isEmpty():
    print("Empty")
else:
    print(f'Number in Queue is :  {q.items}')
    #print(f'Number in Queue is : {q.items}')