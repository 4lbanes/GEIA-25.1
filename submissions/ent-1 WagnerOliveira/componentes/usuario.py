from componentes.livro import Livro


class Usuario:
    """
    Classe que representa um usuário do sistema da biblioteca.
    """
    def __init__(self, nome, email):
        """
        Inicializa um objeto Usuario.

        Args:
            nome (str): O nome do usuário.
            email (str): O email do usuário.
        """
        if not isinstance(nome, str) or not nome:
            raise ValueError("Nome deve ser uma string não vazia.")
        if not isinstance(email, str) or not email:
            raise ValueError("Email deve ser uma string não vazia.")
        if '@' not in email or '.' not in email:
            raise ValueError("Email deve ser um email válido.")

        self.nome = nome
        self.email = email
        self.livros_emprestados = []  # Lista de livros emprestados pelo usuário

    def __str__(self):
        """
        Retorna uma representação em string do usuário.
        """
        return f"Nome: {self.nome}, Email: {self.email}, Livros Emprestados: {len(self.livros_emprestados)}"

    def __repr__(self):
        """
        Retorna uma representação oficial em string do usuário.
        """
        return f"Usuario(nome='{self.nome}', email='{self.email}')"

    def pegar_livro(self, livro):
        """
        Adiciona um livro à lista de livros emprestados do usuário.

        Args:
            livro (Livro): O livro a ser adicionado.
        """
        if not isinstance(livro, Livro):
            raise TypeError("Livro deve ser um objeto da classe Livro.")
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        """
        Remove um livro da lista de livros emprestados do usuário.

        Args:
            livro (Livro): O livro a ser removido.
        """
        if not isinstance(livro, Livro):
            raise TypeError("Livro deve ser um objeto da classe Livro.")
        if livro not in self.livros_emprestados:
            raise ValueError(f"Livro '{livro.titulo}' não está na lista de livros emprestados de {self.nome}.")
        self.livros_emprestados.remove(livro)

# Abstração
class UsuarioRegular(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.max_livros = 3

    def pode_emprestar(self):
      return len(self.livros_emprestados) < self.max_livros

class UsuarioVIP(Usuario):
    def __init__(self, nome, email):
        super().__init__(nome, email)
        self.max_livros = 5  # Pode emprestar mais livros [cite: 20]
        self.prazo_devolucao = 14 # Prazo de devolução mais longo (exemplo) [cite: 20]

    def pode_emprestar(self):
      return len(self.livros_emprestados) < self.max_livros