class Node:
    # Essa classe representa um nó de uma lista encadeada. Cada nó contém dados e um ponteiro para o próximo nó.
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Essa classe representa uma lista encadeada. Ela contém métodos para adicionar, remover e encontrar nós na lista.
    # Ela também possui um método para iterar sobre os nós da lista e sempre começa do nó cabeça (head).
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
        if not self.head:  # Se a lista estiver vazia, não há nada para remover.
            return
        if self.head.data == data:  # Se o dado a ser removido está na cabeça, atualiza a cabeça.
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:  # Percorre a lista até encontrar o nó a ser removido.
            current = current.next
        if current.next:  # Se encontrou o nó, remove-o ajustando os ponteiros.
            current.next = current.next.next

    def find(self, condition):
        results = []  # Lista para armazenar os resultados que atendem à condição.
        current = self.head
        while current:  # Percorre todos os nós da lista.
            print(f"Verificando: {current.data.get_titulo()} - {current.data.get_autor()}")  # Depuração.
            if condition(current.data):  # Verifica se o dado atende à condição.
                results.append(current.data)
            current = current.next
        return results  # Retorna todos os dados que atendem à condição.

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next