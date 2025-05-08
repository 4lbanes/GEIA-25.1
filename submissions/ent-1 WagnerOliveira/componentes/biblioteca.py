from componentes.livro import Livro
from componentes.usuario import Usuario


class Biblioteca:
    """
    Classe que representa o sistema de gerenciamento da biblioteca.
    """
    def __init__(self):
        """
        Inicializa um objeto Biblioteca.
        """
        self.livros = []  # Lista de todos os livros na biblioteca
        self.usuarios = []  # Lista de todos os usuários da biblioteca


    def adicionar_livro(self, livro):
        """
        Adiciona um livro ao sistema da biblioteca.

        Args:
            livro (Livro): O livro a ser adicionado.
        """
        if not isinstance(livro, Livro):
            raise TypeError("Livro deve ser um objeto da classe Livro.")
        self.livros.append(livro)


    def adicionar_usuario(self, usuario):
        """
        Adiciona um usuário ao sistema da biblioteca.

        Args:
            usuario (Usuario): O usuário a ser adicionado.
        """
        if not isinstance(usuario, Usuario):
            raise TypeError("Usuario deve ser um objeto da classe Usuario.")
        self.usuarios.append(usuario)


    def buscar_livro(self, termo):
        """
        Busca livros por título ou autor.

        Args:
            termo (str): O termo de busca (título ou autor).

        Returns:
            list: Uma lista de livros que correspondem ao termo de busca.
        """
        if not isinstance(termo, str):
            raise TypeError("Termo de busca deve ser uma string.")
        if not termo:
            return [] # Retorna lista vazia se o termo for vazio

        resultados = []
        for livro in self.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower():
                resultados.append(livro)
        return resultados


    def emprestar_livro(self, livro_titulo, usuario_email):
        """
        Empresta um livro para um usuário.

        Args:
            livro_titulo (str): O título do livro a ser emprestado.
            usuario_email (str): O email do usuário que está pegando o livro.
        """
        if not isinstance(livro_titulo, str):
            raise TypeError("Título do livro deve ser uma string.")
        if not isinstance(usuario_email, str):
            raise TypeError("Email do usuário deve ser uma string.")

        livro_para_emprestar = None
        for livro in self.livros:
            if livro.titulo == livro_titulo:
                livro_para_emprestar = livro
                break

        if livro_para_emprestar is None:
            raise ValueError(f"Livro com título '{livro_titulo}' não encontrado.")

        usuario_para_emprestar = None
        for usuario in self.usuarios:
            if usuario.email == usuario_email:
                usuario_para_emprestar = usuario
                break

        if usuario_para_emprestar is None:
            raise ValueError(f"Usuário com email '{usuario_email}' não encontrado.")

        if livro_para_emprestar.status == "disponível":
            livro_para_emprestar.emprestar()
            usuario_para_emprestar.pegar_livro(livro_para_emprestar)
            print(f"Livro '{livro_para_emprestar.titulo}' emprestado para {usuario_para_emprestar.nome}.")
        else:
            print(f"Livro '{livro_para_emprestar.titulo}' não está disponível.")


    def devolver_livro(self, livro_titulo, usuario_email):
        """
        Devolve um livro para a biblioteca.

        Args:
            livro_titulo (str): O título do livro a ser devolvido.
            usuario_email (str): O email do usuário que está devolvendo o livro.
        """
        if not isinstance(livro_titulo, str):
            raise TypeError("Título do livro deve ser uma string.")
        if not isinstance(usuario_email, str):
            raise TypeError("Email do usuário deve ser uma string.")

        livro_para_devolver = None
        for livro in self.livros:
            if livro.titulo == livro_titulo:
                livro_para_devolver = livro
                break

        if livro_para_devolver is None:
            raise ValueError(f"Livro com título '{livro_titulo}' não encontrado.")

        usuario_para_devolver = None
        for usuario in self.usuarios:
            if usuario.email == usuario_email:
                usuario_para_devolver = usuario
                break

        if usuario_para_devolver is None:
            raise ValueError(f"Usuário com email '{usuario_email}' não encontrado.")

        try:
            livro_para_devolver.devolver()
            usuario_para_devolver.devolver_livro(livro_para_devolver)
            print(f"Livro '{livro_para_devolver.titulo}' devolvido por {usuario_para_devolver.nome}.")
        except ValueError as e:
            print(e)  # Imprime a mensagem de erro


    def relatorio_livros_emprestados(self):
        """
        Gera um relatório de todos os livros emprestados.

        Returns:
            list: Uma lista de strings, onde cada string contém informações sobre um livro emprestado.
        """
        relatorio = []
        for usuario in self.usuarios:
            for livro in usuario.livros_emprestados:
                relatorio.append(f"Livro: {livro.titulo}, Autor: {livro.autor}, Usuário: {usuario.nome}, Email: {usuario.email}")
        return relatorio
