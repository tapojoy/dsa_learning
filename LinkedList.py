class SinglyLinkedListElement:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def set_key(self, key):
        self.key = key

    def set_next(self, element):
        self.next = element

    def get_key(self):
        return self.key

    def get_next(self):
        return self.next

    def is_none(self):
        if not self.key:
            return True
        return False

    def set_none(self):
        self.key = None
        self.next = None


class DoublyLinkedListElement(SinglyLinkedListElement):
    def __init__(self, key=None):
        super().__init__(key)
        self.prev = None

    def set_prev(self, element):
        self.prev = element

    def get_prev(self):
        return self.prev

    def set_none(self):
        super().set_none()
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = SinglyLinkedListElement()

    def insert(self, key):
        if not key:
            return
        if self.head.is_none():
            self.head.set_key(key)
        else:
            new_element = SinglyLinkedListElement(key)
            new_element.set_next(self.head)
            self.head = new_element

    def search_key(self, key):
        if not key:
            return None
        x = self.head
        while True:
            if x.get_key() == key:
                return x
            x = x.get_next()
            if not x:
                return None

    def delete_node(self, key):
        node = self.search_key(key)
        if not isinstance(node, SinglyLinkedListElement):
            return False
        if node is self.head:
            self.head = node.get_next()
            node.set_none()
            return True
        x = self.head
        while x.get_next() is not node:
            x = x.get_next()
        if not node.get_next():
            x.set_next(None)
        else:
            x.set_next(node.get_next())
        node.set_none()
        return True


class DoublyLinkedList:
    def __init__(self):
        self.head = DoublyLinkedListElement()

    def insert(self, key):
        if not key:
            return
        if self.head.is_none():
            self.head.set_key(key)
        else:
            new_element = DoublyLinkedListElement(key)
            new_element.set_next(self.head)
            self.head.set_prev(new_element)
            self.head = new_element

    def search_key(self, key):
        if not key:
            return None
        x = self.head
        while True:
            if x.get_key() == key:
                return x
            x = x.get_next()
            if not x:
                return None

    def delete_node(self, key):
        node = self.search_key(key)
        if not isinstance(node, DoublyLinkedListElement):
            return False
        if node is self.head:
            self.head = node.get_next()
            node.set_none()
            return True
        if not node.get_next():
            node.get_prev().set_next(None)
        else:
            node.get_prev().set_next(node.get_next())
            node.get_next().set_prev(node.get_prev())
        node.set_none()
        return True


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.head.set_prev(self.head)
        self.head.set_next(self.head)

    def insert(self, key):
        if not key:
            return
        new_element = DoublyLinkedListElement(key)
        new_element.set_next(self.head.get_next())
        self.head.get_next().set_prev(new_element)
        self.head.set_next(new_element)
        new_element.set_prev(self.head)

    def search_key(self, key):
        if not key:
            return None
        x = self.head.get_next()
        if x is self.head:
            return None
        while True:
            if x.get_key() == key:
                return x
            x = x.get_next()
            if x is self.head:
                return None

    def delete_node(self, key):
        node = self.search_key(key)
        if not isinstance(node, DoublyLinkedListElement):
            return False
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        node.set_none()
        return True


class StackUsingSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def push(self, key):
        super().insert(key)

    def pop(self):
        if self.head.is_none():
            return None
        popped = self.head.get_key()
        x = self.head.get_next()
        self.head.set_none()
        if x:
            self.head = x
        return popped


class QueueUsingSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = self.head

    def enqueue(self, key):
        if not key:
            return
        if self.tail.is_none():
            self.tail.set_key(key)
        else:
            new_element = SinglyLinkedListElement(key)
            self.tail.set_next(new_element)
            self.tail = new_element

    def dequeue(self):
        if self.head.is_none():
            return None
        dequeued = self.head.get_key()
        x = self.head.get_next()
        self.head.set_none()
        if x:
            self.head = x
        return dequeued
