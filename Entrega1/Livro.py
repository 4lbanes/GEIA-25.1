from abc import ABC, abstractmethod

'''Interface Livro'''
class Livro(ABC):

    @abstractmethod
    def __init__(self, titulo, autor, ano_publicacao):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def get_titulo(self):
        pass

    @abstractmethod
    def get_autor(self):
        pass

    @abstractmethod
    def get_ano_publicacao(self):
        pass