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
    def __init__(self, head_key):
        self.head = SinglyLinkedListElement()
        self.head.set_key(head_key)
        self.tail = self.head

    def insert_at_tail(self, key):
        if not key:
            return
        new_element = SinglyLinkedListElement()
        new_element.set_key(key)
        self.tail.set_next(new_element)
        self.tail = new_element

    def insert_at_head(self, key):
        if not key:
            return
        new_element = SinglyLinkedListElement()
        new_element.set_key(key)
        new_element.set_next(self.head)
        self.head = new_element

    def search_key(self, key):
        x = self.head
        while True:
            if x.get_key() == key:
                return x
            x = x.get_next()
            if not x:
                return None

    def delete_node(self, key):
        if self.head is self.tail:
            return False
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
        if node is self.tail:
            x.set_next(None)
            self.tail = x
        else:
            x.set_next(node.get_next())
        node.set_none()
        return True


class DoublyLinkedList(SinglyLinkedList):
    def __init__(self, head_key):
        super().__init__(head_key)
        self.head = DoublyLinkedListElement()
        self.head.set_key(head_key)
        self.tail = self.head

    def insert_at_tail(self, key):
        new_element = DoublyLinkedListElement()
        new_element.set_key(key)
        new_element.set_prev(self.tail)
        self.tail.set_next(new_element)
        self.tail = new_element

    def insert_at_head(self, key):
        new_element = DoublyLinkedListElement()
        new_element.set_key(key)
        new_element.set_next(self.head)
        self.head.set_prev(new_element)
        self.head = new_element

    def delete_node(self, key):
        if self.head is self.tail:
            return False
        node = self.search_key(key)
        if not isinstance(node, DoublyLinkedListElement):
            return False
        if node is self.head:
            self.head = node.get_next()
            self.head.set_prev(None)
            node.set_none()
            return True
        if node is self.tail:
            self.tail = node.get_prev()
            self.tail.set_next(None)
            node.set_none()
            return True
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        node.set_none()
        return True


class CircularDoublyLinkedList(DoublyLinkedList):
    def __init__(self, head_key):
        super().__init__(head_key)
        self.head.set_next(self.head)
        self.head.set_prev(self.head)
        self.tail = self.head

    def insert_at_tail(self, key):
        super().insert_at_tail(key)
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)

    def insert_at_head(self, key):
        super().insert_at_head(key)
        self.head.set_prev(self.tail)
        self.tail.set_next(self.head)

    def search_key(self, key):
        x = self.head
        while True:
            if x.get_key() == key:
                return x
            x = x.get_next()
            if not x:
                return None
            if x is self.head:
                return None

    def delete_node(self, key):
        if self.head is self.tail:
            return False
        node = self.search_key(key)
        if not isinstance(node, DoublyLinkedListElement):
            return False
        if node is self.head:
            self.head = node.get_next()
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)
            node.set_none()
            return True
        if node is self.tail:
            self.tail = node.get_prev()
            self.tail.set_next(self.head)
            self.head.set_prev(self.tail)
            node.set_none()
            return True
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        node.set_none()
        return True


class StackUsingSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__(None)

    def push(self, key):
        super().insert_at_head(key)

    def pop(self):
        if self.head is self.tail:
            return None
        popped = self.head.get_key()
        x = self.head.get_next()
        self.head.set_none()
        self.head = x
        return popped


class QueueUsingSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__(None)
        
    def enqueue(self, key):
        super().insert_at_tail(key)
        if self.head.is_none():
            self.head = self.tail
        
    def dequeue(self):
        if self.head.is_none():
            return None
        dequeued = self.head.get_key()
        x = self.head.get_next()
        self.head.set_none()
        if x:
            self.head = x
        return dequeued
