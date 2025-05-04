from models.livro import LivroFisico, LivroDigital
from models.usuario import Usuario, UsuarioVIP
from models.biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Cadastramento de livros... 
    livro1 = LivroFisico("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
    livro2 = LivroDigital("Python para Iniciantes", "Guido van Rossum", 2020)
    livro3 = LivroFisico("Clean Code", "Robert C. Martin", 2008)
    biblioteca.cadastrar_livro(livro1)
    biblioteca.cadastrar_livro(livro2)
    biblioteca.cadastrar_livro(livro3)

    # Cadastramento de usuários... 
    usuario1 = Usuario("Marcos", "marcos@example.com")
    usuario2 = UsuarioVIP("Ana", "ana@example.com")
    biblioteca.cadastrar_usuario(usuario1)
    biblioteca.cadastrar_usuario(usuario2)

    # Empréstimo de livros
    biblioteca.emprestar_livro(livro1, usuario1)
    biblioteca.emprestar_livro(livro2, usuario2)

    # Tentativa de emprestar um livro já emprestado
    print("\nTentativa de emprestar um livro já emprestado:")
    biblioteca.emprestar_livro(livro1, usuario2)

    # Relatório de empréstimos
    print("\nRelatório de empréstimos:")
    print(biblioteca.relatorio_emprestimos())

    # Devolução de livro
    print("\nDevolvendo livro:")
    biblioteca.devolver_livro(livro1, usuario1)
    print(f"Livro '{livro1.get_titulo()}' devolvido por {usuario1.get_nome()}.")

    # Relatório atualizado
    print("\nRelatório atualizado de empréstimos:")
    print(biblioteca.relatorio_emprestimos())

    # Busca de livros
    print("\nBusca de livros por título:")
    resultados = biblioteca.buscar_livro("Python")
    for livro in resultados:
        print(f"Encontrado: {livro.get_titulo()} - {livro.get_autor()}")

if __name__ == "__main__":
    main()