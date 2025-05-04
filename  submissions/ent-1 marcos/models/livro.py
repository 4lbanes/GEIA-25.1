from abc import ABC, abstractmethod


class Livro(ABC):
    def __init__(self, titulo, autor, ano, status="disponível"):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__status = status  # Certifique-se de que este atributo seja inicializado

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    @abstractmethod
    def tipo(self):
        pass


class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)  # Chama o construtor da classe base

    def tipo(self):
        return "Físico"


class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)  # Chama o construtor da classe base

    def tipo(self):
        return "Digital"