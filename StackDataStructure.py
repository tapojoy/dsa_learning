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
