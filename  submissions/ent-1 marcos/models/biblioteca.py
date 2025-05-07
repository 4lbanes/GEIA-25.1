from models.livro import LivroFisico, LivroDigital
from models.usuario import Usuario, UsuarioVIP
from models.helpers.node import LinkedList

class Biblioteca:
    #Aqui está a classe da biblioteca, com atributos e métodos para gerenciar os livros e usuários. 
    #Ela utiliza a classe LinkedList para armazenar os livros e usuários.
    #Dentro dela tem as classes Livro e Usuario, que são responsáveis por gerenciar os livros e usuários respectivamente.

    def __init__(self):
        self.__livros = LinkedList()
        self.__usuarios = LinkedList()

    def cadastrar_livro(self, livro):
        self.__livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def buscar_livro(self, criterio):
        criterio = criterio.strip().lower()  # Remove espaços extras e converte para minúsculas (Usei IA aqui para achar a solução...)
        return self.__livros.find(
            lambda livro: criterio in livro.get_titulo().strip().lower() or criterio in livro.get_autor().strip().lower()
        )

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