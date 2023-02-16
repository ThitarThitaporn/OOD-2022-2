class QueueDeque:
    def __init__(self) -> None:
        self.items = deque()
    
    def deQueue(self):
        return self.items.popleft()
    
    def enQueue(self,data):
        self.items.append(data)
        
    def isEmpty(self):
        return len(self.items) == 0
    
class QueueList:
    def __init__(self) -> None:
        self.items = list()
    
    def deQueue(self):
        return self.items.pople()
    
    def enQueue(self,data):
        self.items.append(data)
        
    def isEmpty(self):
        return len(self.items) == 0
    
QueueDeque = QueueDeque()
qList = QueueList()
for i in range(1000):
    