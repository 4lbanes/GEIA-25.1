import sys
import os

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.livro import LivroFisico, LivroDigital
from models.usuario import Usuario, UsuarioVIP
from models.biblioteca import Biblioteca

def test_biblioteca():
    # Criando a biblioteca
    biblioteca = Biblioteca()

    # Testando cadastro de livros
    livro1 = LivroFisico("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro2 = LivroDigital("Python para Iniciantes", "Guido van Rossum", 2020)
    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)

    # Testando cadastro de usuários
    usuario1 = Usuario("Marcos", "marcos@example.com")
    usuario2 = UsuarioVIP("Ana", "ana@example.com")
    biblioteca.cadastrar_usuario(usuario1)
    biblioteca.cadastrar_usuario(usuario2)

    # Testando empréstimo de livro
    biblioteca.emprestar_livro(livro1, usuario1)
    assert livro1.get_status() == "emprestado"
    assert livro1 in usuario1.get_livros_emprestados()

    # Testando devolução de livro
    biblioteca.devolver_livro(livro1, usuario1)
    assert livro1.get_status() == "disponível"
    assert livro1 not in usuario1.get_livros_emprestados()

    # Testando busca de livros
    resultados = biblioteca.buscar_livro("Python")
    assert len(resultados) == 1
    assert resultados[0].get_titulo() == "Python para Iniciantes"

    # Testando relatório de empréstimos
    biblioteca.emprestar_livro(livro2, usuario2)
    relatorio = biblioteca.relatorio_emprestimos()
    assert len(relatorio) == 1
    assert relatorio[0] == ("Python para Iniciantes", "Ana")

    print("Todos os testes passaram!")

if __name__ == "__main__":
    test_biblioteca()

def buscar_livro(self, criterio):
    criterio = criterio.lower()  # Ignorar maiúsculas/minúsculas
    return self.__livros.find(lambda livro: criterio in livro.get_titulo().lower() or criterio in livro.get_autor().lower())