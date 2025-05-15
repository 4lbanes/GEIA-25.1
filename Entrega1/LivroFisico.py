from Livro import Livro

'''Classe Livro Fisico'''
class LivroFisico(Livro):
    
    def __init__(self, titulo, autor, ano_publicacao):
        super().__init__(titulo, autor, ano_publicacao)
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__disponivel = True

    def emprestar(self):
        self.__disponivel = False
    
    def devolver(self):
        self.__disponivel = True
    
    def status(self):
        return self.__disponivel

    '''Métodos Getters'''   
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_ano_publicacao(self):
        return self.__ano_publicacao
    
    def __str__(self):
        return self.__titulo
        