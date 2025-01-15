class QueueDataStructure:
    def __init__(self, size):
        self.size = size
        self.queue = []
        for i in range(self.size): self.queue.append(None)
        self.head = 0
        self.tail = 0

    def is_queue_full(self):
        if self.tail == self.head and self.queue[self.tail] is not None:
            return True
        return False

    def is_queue_empty(self):
        if self.head == self.tail and self.queue[self.tail] is None:
            return True
        return False

    def enqueue(self, element):
        if self.is_queue_full():
            return False
        self.queue[self.tail] = element
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        return True

    def dequeue(self):
        if self.is_queue_empty():
            return None
        element = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return element
