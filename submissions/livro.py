from abc import abstractmethod, ABC

class Livro(ABC):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo  
        self.autor = autor 
        self.ano = ano 
        self._status = True  # Status do livro (True = disponível, False = emprestado)
    
    @property
    def status(self):
        return self._status
    
    @abstractmethod
    def tipo(self):
        pass

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Tipo: {self.tipo}, {'Disponível' if self.status else 'Indisponível'}"

class LivroFisico(Livro):
    @property
    def tipo(self):
        return "físico"
    
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)

class LivroDigital(Livro):
    @property
    def tipo(self):
        return "digital"

    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor, ano)