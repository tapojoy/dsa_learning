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

class DequeDataStructure(QueueDataStructure):
    def __init__(self, size):
        super().__init__(size)

    def enqueue_at_tail(self, element):
        return self.enqueue(element)

    def dequeue_at_head(self):
        return self.dequeue()

    def enqueue_at_head(self, element):
        if self.is_queue_full():
            return False
        if self.head == 0:
            self.head = self.size - 1
        else:
            self.head -= 1
        self.queue[self.head] = element
        return True

    def dequeue_at_tail(self):
        if self.is_queue_empty():
            return None
        if self.tail == 0:
            self.tail = self.size - 1
        else:
            self.tail -= 1
        element = self.queue[self.tail]
        self.queue[self.tail] = None
        return element

