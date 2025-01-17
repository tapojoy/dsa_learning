class StackDataStructure:
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = 0
        for i in range(self.size): self.stack.append(None)

    def is_stack_empty(self):
        if self.top == 0:
            return True
        return False

    def is_stack_full(self):
        if self.top == self.size:
            return True
        return False

    def push_to_stack(self, element):
        if self.is_stack_full():
            return False # stack overflow
        self.stack[self.top] = element
        self.top += 1
        return True

    def pop_from_stack(self):
        if self.is_stack_empty():
            return None # stack underflow
        self.top -= 1
        popped = self.stack[self.top]
        self.stack[self.top] = None
        return popped


class StackDataStructureTwo(StackDataStructure):
    def __init__(self, size):
        super().__init__(size)
        self.top2 = self.size - 1

    def is_stack2_empty(self):
        if self.top2 == self.size - 1:
            return True
        return False

    def is_stack2_full(self):
        if self.top2 < 0:
            return True
        return False

    def are_stacks_overlapping(self):
        if self.top > self.top2:
            return True
        return False

    def push_to_stack2(self, element):
        if self.is_stack2_full() or self.are_stacks_overlapping():
            return False
        self.stack[self.top2] = element
        self.top2 -= 1
        return True

    def pop_from_stack2(self):
        if self.is_stack2_empty():
            return None
        self.top2 += 1
        popped = self.stack[self.top2]
        self.stack[self.top2] = None
        return popped

    def push_to_stack(self, element):
        if self.is_stack_full() or self.are_stacks_overlapping():
            return False
        self.stack[self.top] = element
        self.top += 1
        return True


class QueueUsingStackDataStructure:
    def __init__(self,size):
        self.size = size
        self.stack1 = StackDataStructure(self.size)
        self.stack2 = StackDataStructure(self.size)

    def enqueue_using_stacks(self, element):
        return self.stack1.push_to_stack(element)

    def dequeue_using_stacks(self):
        if self.stack1.is_stack_empty():
            return None
        top = self.stack1.top
        while top > 1:
            self.stack2.push_to_stack(self.stack1.pop_from_stack())
            top -= 1
        popped = self.stack1.pop_from_stack()
        top = self.stack2.top
        while top > 0:
            self.stack1.push_to_stack(self.stack2.pop_from_stack())
            top -= 1
        return popped
