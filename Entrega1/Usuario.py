from abc import ABC, abstractmethod

class Usuario(ABC):

    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    @abstractmethod
    def livros_emprestados(self):
        pass
    
    @abstractmethod
    def alugar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass
    
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_email(self):
        pass