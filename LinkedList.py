class LinkedListElement:
    def __init__(self):
        self.key = None
        self.prev = None
        self.next = None

    def set_key(self, key):
        self.key = key

    def set_next(self, element):
        self.next = element

    def set_prev(self, element):
        self.prev = element

    def get_key(self):
        return self.key

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self, head_key):
        self.head = LinkedListElement()
        self.head.set_key(head_key)
        self.tail = self.head

    def insert_at_tail(self, key):
        new_element = LinkedListElement()
        new_element.set_key(key)
        new_element.set_prev(self.tail)
        self.tail.set_next(new_element)
        self.tail = new_element

    def insert_at_head(self, key):
        new_element = LinkedListElement()
        new_element.set_key(key)
        new_element.set_next(self.head)
        self.head.set_prev(new_element)
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
        if not isinstance(node, LinkedListElement):
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
