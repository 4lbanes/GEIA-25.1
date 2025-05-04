class Usuario:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_livros_emprestados(self):
        return self.__livros_emprestados

    def adicionar_livro(self, livro):
        self.__livros_emprestados.append(livro)

    def remover_livro(self, livro):
        self.__livros_emprestados.remove(livro)


class UsuarioVIP(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.__limite = 10

    def get_limite(self):
        return self.__limite