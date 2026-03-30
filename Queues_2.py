class Queue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.size = size
        self.available = size

    def enqueue(self, item):
        if self.available == 0:
            print*("Queue Overflow")
        else:
            self.queue[self.rear] = item
            self.rear = (self.rear+1)%self.size
            self.available -= 1

    def dequeue(self):
        if self.available == self.size:
            print("Queue Underflow")
        else:
            self.queue[self.front] = None
            self.front = (self.front+1)%self.size
            self.available += 1
        
    def peek(self):
        print("Front (Peek):", self.queue[self.front])
    def getRear(self):
        print("Rear:", self.queue[self.rear-1])

    def print_queue(self):
        print("Queue:", self.queue)

q = Queue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

q.dequeue()
q.dequeue()

q.peek()
q.getRear()

q.print_queue()