class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def push(self,value):
        if self.isFull():
            print("Queue is full")
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value
    
    def pop(self):
        if self.isEmpty():
            print("Queue is empty")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def print(self):
        if self.isEmpty():
            print("queue is empty")
        else:
            i = self.front
            while i != self.rear:
                print(self.queue[i], end = " ")
                i = (i + 1) % self.size
            print(self.queue[self.rear])

q = CircularQueue(5)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.print()
print(q.pop())
q.print()
q.push(6)
q.print()
q.pop()
q.push(7)
q.print()

