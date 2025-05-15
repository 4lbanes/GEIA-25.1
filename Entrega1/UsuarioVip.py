from Usuario import Usuario
from LinkedList import LinkedList
from LivroFisico import LivroFisico

class UsuarioVip(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.__livros_emprestados = LinkedList(7)

    def livros_emprestados(self):
        return self.__livros_emprestados
    
    def alugar(self, livro):
        self.__livros_emprestados.add(livro)
        if isinstance(livro, LivroFisico):
            livro.emprestar()
    
    def devolver(self, livro):
        self.__livros_emprestados.remove_by_name(self.__livros_emprestados.search_node(livro))
        if isinstance(livro, LivroFisico):
            livro.devolver()

    def get_email(self):
        return self._email
    
    def get_nome(self):
        return self._nome

    def __str__(self):
        return self._nome