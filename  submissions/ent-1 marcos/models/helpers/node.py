class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, condition):
        results = []
        current = self.head
        while current:
            print(f"Verificando: {current.data.get_titulo()} - {current.data.get_autor()}")  # Adicionado para depuração
            if condition(current.data):
                results.append(current.data)
            current = current.next
        return results

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next