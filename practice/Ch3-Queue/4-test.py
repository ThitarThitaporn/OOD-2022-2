class Queue :
    def __init__(self,item=None):
        if item == None :
            self.item = []
        else :
            self.item = item
    def enQueue(self,item):
        self.item.append(item)
    def deQueue(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.item == []

inp,op = input('Enter Input : ').split('/')
lst = dict()
for i in inp.split(','):
    i = i.split() 
    lst[i[1]] = i[0]
queue = Queue()
for d in op.split(','):
    d = d.split()
    if d[0] == 'D':
        if queue.isEmpty():
            print("Empty")
        else:
            print(int(queue.deQueue()[1]))
    elif d[0] == 'E':
        d[0] = lst[d[1]]
        queue.enQueue(d)
