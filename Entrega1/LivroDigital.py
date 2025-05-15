from Livro import Livro

'''Classe Livro Digital'''
class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, link):
        super().__init__(titulo, autor, ano_publicacao)
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__link = link

    def status(self):
        return True
    
    '''Métodos Getters'''
    def get_link(self):
        return self.__link
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    
    def __str__(self):
        return self.__titulo