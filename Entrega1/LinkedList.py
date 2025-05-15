'''Lista encadeada'''
class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

class LinkedList:
    def __init__(self, max_size=None):
        if max_size is not None:
            self.__size = 0
            self.__head = None
            self.max_size = max_size
        else:
            self.__size = 0
            self.__head = None
    
    def insert(self, value):
        new_node = Node(value)
        if(self.__size != 0):
            new_node.next = self.__head
        self.__head = new_node
        self.__size += 1

    def add(self, value):
        if(self.__size == 0):
            self.insert(value)
        else:
            new_node = Node(value)
            aux_node = self.__head
            while(aux_node.next != None):
                aux_node = aux_node.next
            aux_node.next = new_node
            self.__size += 1
    
    def __is_empty(self):
        if (self.__size == 0):
            raise IndexError("EmptyList")
    
    def remove_by_name(self, name):
        aux_node = self.__head
        if self.__size == 1:
            self.remove_first()
        else:           
            for i in range(self.__size):
                if str(aux_node.next) == name:
                    aux_node2 = aux_node.next
                    aux_node.next = aux_node.next.next
                    self.__size -= 1
                    return aux_node2
    
    def size(self):
        return self.__size
    
    def remove_first(self):
        self.__is_empty()
        to_be_removed = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return to_be_removed
    
    def search_node(self, node):
        aux_node = self.__head
        for i in range(self.__size):
            if node == str(aux_node):
                return aux_node.value
            aux_node = aux_node.next
        return "Não foi encontrado"
    
    def search_node_all(self, node):
        aux_node = self.__head
        lista = []
        for i in range(self.__size):
            if node in str(aux_node):
                lista.append(aux_node.value)
            aux_node = aux_node.next
        if lista == []:
            return "Não foi encontrado"
        else:
            return lista
    
    def __iter__(self):
        self.__iter_node = self.__head
        return self

    def __next__(self):
        if self.__iter_node is None:
            raise StopIteration
        else:
            current = self.__iter_node
            self.__iter_node = self.__iter_node.next
            return current.value
    
    def __str__(self):
        listData = "[ "
        aux_node = self.__head
        for i in range(self.__size):
            listData += str(aux_node)
            aux_node = aux_node.next
            if (i < self.__size-1):
                listData += ", "
        return listData + " ]"