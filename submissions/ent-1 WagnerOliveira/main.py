from componentes.livro import Livro, LivroDigital, LivroFisico
from componentes.biblioteca import Biblioteca
from componentes.usuario import UsuarioRegular, UsuarioVIP


# Exemplo de uso
biblioteca = Biblioteca()

# Criando livros
livro1 = LivroFisico("Dom Quixote", "Miguel de Cervantes", 1605, "A1-23")
livro2 = LivroDigital("1984", "George Orwell", 1949, "www.exemplo.com/1984.pdf")
livro3 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Criando usuários
usuario1 = UsuarioRegular("Alice", "alice@email.com")
usuario2 = UsuarioVIP("Bob", "bob@email.com")

biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Empréstimo
biblioteca.emprestar_livro(livro1.titulo, usuario1.email)
biblioteca.emprestar_livro(livro2.titulo, usuario1.email)
biblioteca.emprestar_livro(livro3.titulo, usuario2.email)

# Relatório
print("Relatório de Livros Emprestados:")
for item in biblioteca.relatorio_livros_emprestados():
    print(item)

# Devolução
biblioteca.devolver_livro(livro1.titulo, usuario1.email)

print("\nRelatório após devolução:")
for item in biblioteca.relatorio_livros_emprestados():
    print(item)

# Busca
print("\nBusca por 'Senhor':")
for livro in biblioteca.buscar_livro("Senhor"):
    print(livro)