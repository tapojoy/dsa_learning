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

    def heap_sort(self):
        self.build_max_heap()
        i = self.size - 1
        while i > 0:
            self.exchange(index1=i, index2=0)
            self.heap_size -= 1
            self.max_heapify(0)
            i -= 1
        self.heap_size = self.size


class MinHeapDataStructure(HeapDataStructure):
    def __init__(self, heap):
        super().__init__(heap)

    def min_heapify(self, i):
        while i < self.heap_size:
            l = self.left(i)
            r = self.right(i)
            if l < self.heap_size:
                if self.heap[i] < self.heap[l]:
                    smallest = i
                else:
                    smallest = l
                if r < self.heap_size:
                    if self.heap[r] < self.heap[smallest]:
                        smallest = r
                if smallest != i:
                    self.exchange(i, smallest)
                    i = smallest
                else:
                    break
            else:
                break

    def build_min_heap(self):
        self.heap_size = self.size
        i = (self.size // 2) - 1
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def heap_sort(self):
        self.build_min_heap()
        i = self.size - 1
        while i > 0:
            self.exchange(index1=i, index2=0)
            self.heap_size -= 1
            self.min_heapify(0)
            i -= 1
        self.heap_size = self.size

