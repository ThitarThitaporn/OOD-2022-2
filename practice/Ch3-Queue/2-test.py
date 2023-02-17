class Queue :

    def __init__(self, list= None):
        if list== None:self.items= []
        else:self.items= list

    def enqueue(self,i):
        self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)   
people = input("Enter people : ")
q = Queue()
for i in range(len(people)):
    q.enqueue(people[i])
  
cashier1 = Queue()
cashier2 = Queue()

start = False
j = 0

for i in range(q.size()):
    if not(cashier1.isEmpty()) and i % 3 == 0 and i !=0:
        cashier1.dequeue()
        
    if not(cashier2.isEmpty()) and j % 2 == 0 and j !=0:
        cashier2.dequeue()
        
    if cashier1.size() >= 5:
        cashier2.enqueue(q.dequeue())
        start =  True
    else:
        cashier1.enqueue(q.dequeue())
        
    if start :
        i += 1
        
    
    print(f'{str(i+1)} {q.items} {cashier1.items} {cashier2.items}')
    
        
        
         
    
            