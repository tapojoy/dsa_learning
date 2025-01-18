class HeapDataStructure:
    def __init__(self, heap):
        self.heap = heap
        self.size = len(heap)
        self.heap_size = self.size

    def exchange(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left(i):
        return (i * 2) + 1

    @staticmethod
    def right(i):
        return (i * 2) + 2


class MaxHeapDataStructure(HeapDataStructure):
    def __init__(self, heap):
        super().__init__(heap)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size:
            if self.heap[i] > self.heap[l]:
                largest = i
            else:
                largest = l
            if r < self.heap_size:
                if self.heap[r] > self.heap[largest]:
                    largest = r
            if largest != i:
                self.exchange(i, largest)
                return self.max_heapify(largest)

    def build_max_heap(self):
        self.heap_size = self.size
        i = (self.size // 2) - 1
        while i >= 0:
            self.max_heapify(i)
            i -= 1
