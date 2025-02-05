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


class CircularSinglyLinkedList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.head.set_next(self.head)

    def insert(self, key):
        if not key:
            return
        new_element = SinglyLinkedListElement(key)
        new_element.set_next(self.head.get_next())
        self.head.set_next(new_element)

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
        if not isinstance(node, SinglyLinkedListElement):
            return False
        x = self.head
        while x.get_next() is not node:
            x = x.get_next()
        x.set_next(node.get_next())
        node.set_none()
        return True


def linked_list_union(l1,l2):
    input_type_tuple = (
        QueueUsingSinglyLinkedList,
        CircularSinglyLinkedList,
        CircularDoublyLinkedList
    )
    error1 = 'inputs should be of same type'
    error2 = 'permitted input types are : ' + str(input_type_tuple)
    assert type(l1) is type(l2), error1
    assert isinstance(l1, input_type_tuple), error2
    if isinstance(l1, QueueUsingSinglyLinkedList):
        if l1.head.is_none():
            return l2
        if l2.head.is_none():
            return l1
        l1.tail.set_next(l2.head)
        l1.tail = l2.tail
        return l1
    if isinstance(l1, CircularSinglyLinkedList):
        x = l1.head.get_next()
        if x is l1.head:
            return l2
        l1.head.set_next(l2.head.get_next())
        l2.head.set_next(x.get_next())
        l2.head.set_key(x.get_key())
        x.set_none()
        return l1
    if isinstance(l1, CircularDoublyLinkedList):
        x = l1.head.get_next()
        l1.head.set_next(l2.head.get_next())
        l2.head.get_next().set_prev(l1.head)
        l2.head.get_prev().set_next(x)
        x.set_prev(l2.head.get_prev())
        x = l2.head
        x.set_none()
        return l1

