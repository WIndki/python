class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1
    
    def isFull(self):
        return (self.rear + 1) % self.size == self.front
    
    def isEmpty(self):
        return self.front == -1
    
    def push(self, value):
        if self.isFull():  # 判断队列是否已满
            raise IndexError("push to full queue")  # 如果队列已满，抛出异常
        elif self.isEmpty():  # 判断队列是否为空
            self.front = 0  # 如果队列为空，front和rear都指向0
            self.rear = 0
            self.queue[self.rear] = value  # 将值插入队列
        else:
            self.rear = (self.rear + 1) % self.size  # rear指针向后移动一位，循环队列取模运算
            self.queue[self.rear] = value  # 将值插入队列
    
    def pop(self):
        if self.isEmpty():  # 判断队列是否为空
            raise IndexError("pop from empty queue")  # 如果队列为空，抛出异常
        elif self.front == self.rear:  # 判断队列是否只有一个元素
            temp = self.queue[self.front]  # 取出队列中的唯一元素
            self.front = -1  # 将front和rear重置为-1，表示队列为空
            self.rear = -1
            return temp  # 返回取出的元素
        else:
            temp = self.queue[self.front]  # 取出队列中的元素
            self.front = (self.front + 1) % self.size  # front指针向后移动一位，循环队列取模运算
            return temp  # 返回取出的元素
    
    def print(self):
        if self.isEmpty():
            raise IndexError("pop from empty queue")
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

