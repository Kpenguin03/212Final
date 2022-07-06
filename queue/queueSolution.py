class dmvQueue:

    def __init__(self):

        self.queue = [] 

    def enqueue(self, value):

        self.queue.append(value)
        

    def dequeue(self):

        value = self.queue[0] 
        del self.queue[0]
        return value





newQueue = dmvQueue()
newQueue.enqueue('Mike')
newQueue.enqueue('Sara')
value = newQueue.dequeue()
print(value)