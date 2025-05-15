from LinkedList import LinkedList
from LivroDigital import LivroDigital
from LivroFisico import LivroFisico 
from UsuarioRegular import UsuarioRegular
from UsuarioVip import UsuarioVip

class Biblioteca:
    def __init__(self):
        self.__lista_de_usuarios = LinkedList()
        self.__lista_de_livros = LinkedList()
        self.__lista_de_livros_emprestados = LinkedList()

    '''Busca e exibe usuários e livros, caso tenha um livro com o mesmo nome ou contenha o nome digitado, ele também irá aparecer'''
    def buscar(self, user_or_book):
        if user_or_book == 2:
            ans = input("\nDigite o nome do usuário: ")
            usuario = self.__lista_de_usuarios.search_node(ans)
            if isinstance(usuario, (UsuarioRegular, UsuarioVip)):
                print(f"\nNome: {usuario.get_nome()}\nEmail: {usuario.get_email()}\nLivros emprestados: {usuario.livros_emprestados()}")
            else:
                print(f"\n{usuario}")
        elif user_or_book == 1:
            ans = input("\nDigite o nome do livro: ")    
            livros = self.__lista_de_livros.search_node_all(ans)
            for livro in livros:
                if isinstance(livro, (LivroDigital, LivroFisico)):
                    print(f"\nNome: {livro.get_titulo()}\nAutor: {livro.get_autor()}\nAno de publicação: {livro.get_ano_publicacao()}\nStatus: {"Disponível" if livro.status() else "Não está disponível"}")
                    if isinstance(livro, (LivroDigital)):
                        print(f"Link: {livro.get_link()}")
                else:
                    print(f"\n{livro}")

    '''Cadastro de livros e usuários'''
    def cadastrar(self, user_or_book):
        if user_or_book == 2:
            print("\n1. VIP")
            print("2. Regular")
            ans = int(input("Deseja ser Vip e pagar ou Regular?"))
            if ans == 1:
                usuario = UsuarioVip(input("\nDigite seu nome: "), input("Digite seu email: "))
            else:
                usuario = UsuarioRegular(input("\nDigite seu nome: "), input("Digite seu email: "))
            self.__lista_de_usuarios.add(usuario)
            print("\nUsuário cadastrado com sucesso!")
        elif user_or_book == 1:
            ans = int(input("\n1. Fisico ou 2. Digital: "))
            if ans == 1:
                livro = LivroFisico(input("\nDigite o título: "), input("Digite o autor: "), int(input("Digite o ano da publicação: ")))
            elif ans == 2:
                livro = LivroDigital(input("\nDigite o título: "), input("Digite o autor: "), int(input("Digite o ano da publicação: ")), input("Digite o link: "))
            self.__lista_de_livros.add(livro)
            print("\nLivro cadastrado com sucesso!")
    
    '''Empresta o livro para o usuário'''
    def emprestar(self, user, book):
        usuario = self.__lista_de_usuarios.search_node(user)
        livro = self.__lista_de_livros.search_node(book)
        if isinstance(usuario, (UsuarioRegular, UsuarioVip)) and isinstance(livro, (LivroFisico, LivroDigital)):
            if self.buscar(usuario) != "Não foi encontrado" and self.buscar(livro) != "Não foi encontrado":
                if livro.status():
                    usuario.alugar(livro)
                    dic = {
                        "usuario": usuario,
                        "livro": livro
                    }
                    self.__lista_de_livros_emprestados.add(dic)
                    print("\nLivro emprestado com sucesso!")
                else:
                    print("\nLivro indisponível")
    
    '''Devolve o livro que estava em posse do usário'''
    def devolver(self, user, book):
        usuario = self.__lista_de_usuarios.search_node(user)
        livro = self.__lista_de_livros.search_node(book)
        if isinstance(usuario, (UsuarioRegular, UsuarioVip)) and isinstance(livro, (LivroFisico, LivroDigital)):
            if self.buscar(usuario) != "Não foi encontrado" and self.buscar(livro) != "Não foi encontrado":
                usuario.devolver(livro)
    
    '''Exibe os livros emprestados e os usuários que alugaram eles'''
    def relatorio(self):
        print()
        for i in self.__lista_de_livros_emprestados:
            print(f"Usuario: {str(i["usuario"])}, Livro: {str(i["livro"])}")