class SinglyLinkedListElement:
    def __init__(self):
        self.key = None
        self.next = None

    def set_key(self, key):
        self.key = key

    def set_next(self, element):
        self.next = element

    def get_key(self):
        return self.key

    def get_next(self):
        return self.next


class DoublyLinkedListElement(SinglyLinkedListElement):
    def __init__(self):
        super().__init__()
        self.prev = None

    def set_prev(self, element):
        self.prev = element

    def get_prev(self):
        return self.prev


class SinglyLinkedList:
    def __init__(self, head_key):
        self.head = SinglyLinkedListElement()
        self.head.set_key(head_key)
        self.tail = self.head

    def insert_at_tail(self, key):
        new_element = SinglyLinkedListElement()
        new_element.set_key(key)
        self.tail.set_next(new_element)
        self.tail = new_element

    def insert_at_head(self, key):
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
            node.set_next(None)
            return True
        x = self.head
        while x.get_next() is not node:
            x = x.get_next()
        if node is self.tail:
            x.set_next(None)
            self.tail = x
            return True
        x.set_next(node.get_next())
        node.set_next(None)
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
            node.set_next(None)
            return True
        if node is self.tail:
            self.tail = node.get_prev()
            self.tail.set_next(None)
            node.set_prev(None)
            return True
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        return True
