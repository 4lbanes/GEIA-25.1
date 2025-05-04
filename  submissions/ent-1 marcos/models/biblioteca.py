from models.livro import LivroFisico, LivroDigital
from models.usuario import Usuario, UsuarioVIP
from models.helpers.node import LinkedList

class Biblioteca:
    def __init__(self):
        self.__livros = LinkedList()
        self.__usuarios = LinkedList()

    def cadastrar_livro(self, livro):
        self.__livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def buscar_livro(self, criterio):
        return self.__livros.find(lambda livro: criterio in (livro.get_titulo(), livro.get_autor()))

    def emprestar_livro(self, livro, usuario):
        if livro.get_status() == "disponível":
            livro.set_status("emprestado")
            usuario.adicionar_livro(livro)
        else:
            print("Livro não disponível.")

    def devolver_livro(self, livro, usuario):
        livro.set_status("disponível")
        usuario.remover_livro(livro)

    def relatorio_emprestimos(self):
        return [(livro.get_titulo(), usuario.get_nome()) for usuario in self.__usuarios for livro in usuario.get_livros_emprestados()]