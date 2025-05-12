from livro import LivroFisico, LivroDigital
from abc import abstractmethod, ABC

class Usuario(ABC):
    def __init__(self, nome, email):
        self._nome = nome  
        self._email = email  
        self.livros_emprestados = []  # Lista de livros físicos emprestados
        self.livro_digital = None  # Livro digital emprestado (apenas 1 permitido)

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    def pegar(self, livro):
        '''Metodo de aluguel do livro, verifica que instancia do livro é e adiciona à variavel adequada para o tipo (livros_emprestados caso fisico e livro_digital caso digital)'''
        if isinstance(livro, LivroFisico):  
            self.livros_emprestados.append(livro) 
        elif isinstance(livro, LivroDigital):
            self.livro_digital = livro 

    def devolver(self, livro):
        '''Metodo de devolução do livro, novamente confere qual a lista em que o livro se encontra e o remove ou muda o valor booleano'''
        if isinstance(livro, LivroFisico): 
            if livro in self.livros_emprestados:
                self.livros_emprestados.remove(livro)  
        elif isinstance(livro, LivroDigital): 
            if self.livro_digital == livro:
                self.livro_digital = None 

    @abstractmethod
    def limite_aluguel(self):
        pass

class UsuarioRegular(Usuario):
    def limite_aluguel(self):
        return 2  
    
class UsuarioVIP(Usuario):
    def limite_aluguel(self):
        return 3  