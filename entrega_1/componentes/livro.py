import datetime


class Livro:
    """
    Classe que representa um livro no sistema da biblioteca.
    """
    def __init__(self, titulo, autor, ano_publicacao):
        """
        Inicializa um objeto Livro.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
            ano_publicacao (int): O ano de publicação do livro.
        """
        if not isinstance(titulo, str) or not titulo:
            raise ValueError("Título deve ser uma string não vazia.")
        if not isinstance(autor, str) or not autor:
            raise ValueError("Autor deve ser uma string não vazia.")
        if not isinstance(ano_publicacao, int):
            raise ValueError("Ano de publicação deve ser um inteiro.")
        if ano_publicacao > datetime.datetime.now().year:
            raise ValueError("Ano de publicação não pode ser maior que o ano atual.")

        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.status = "disponível"  # Status inicial do livro

    def __str__(self):
        """
        Retorna uma representação em string do livro.
        """
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano_publicacao}, Status: {self.status}"

    def __repr__(self):
        """
        Retorna uma representação oficial em string do livro (útil para debugging).
        """
        return f"Livro(titulo='{self.titulo}', autor='{self.autor}', ano_publicacao={self.ano_publicacao})"

    def emprestar(self):
        """
        Muda o status do livro para "emprestado".
        """
        if self.status == "disponível":
            self.status = "emprestado"
        else:
            raise ValueError(f"Livro '{self.titulo}' não está disponível para empréstimo.")

    def devolver(self):
        """
        Muda o status do livro para "disponível".
        """
        if self.status == "emprestado":
            self.status = "disponível"
        else:
            raise ValueError(f"Livro '{self.titulo}' já está disponível.")
        
    # Encapsulamento
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        if novo_status in ["disponível", "emprestado"]: # Validação [cite: 24]
            self._status = novo_status
        else:
            print("Status inválido.")

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({self.ano_publicacao}) - {self.status}"
    
# Abstração
class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano_publicacao, localizacao_prateleira):
        super().__init__(titulo, autor, ano_publicacao)
        self.localizacao_prateleira = localizacao_prateleira

    def __str__(self):
        return f"{super().__str__()} - Localização: {self.localizacao_prateleira}"


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, link_download):
        super().__init__(titulo, autor, ano_publicacao)
        self.link_download = link_download

    def __str__(self):
        return f"{super().__str__()} - Download: {self.link_download}"
