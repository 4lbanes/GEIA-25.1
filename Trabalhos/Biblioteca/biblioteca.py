class Biblioteca:
    def __init__(self):
        self.livros_cadastrados = []
        self.usuarios_cadastrados = []

    def exibirUsuarios(self):

        if not self.usuarios_cadastrados:
            print("Não há nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios_cadastrados:
                print(f"Nome: {usuario.nome} , E-mail: {usuario.email} , Livros: {usuario.emprestados}")
    
    def adicionarUsuario(self):

        nome = input("Qual o seu nome completo? ")
        email = input("E-mail para contato? ")
        novo_usuario = Usuario(nome, email, [])
        self.usuarios_cadastrados.append(novo_usuario)
        print(f"Usuário cadastrado com sucesso, bem-vindo {nome}")

    def adicionarLivro(self):

        titulo = input("Qual o nome do livro a ser adicionado? ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        nome = input("Qual seu nome completo? ")

        usuario_cadastrado = None

        for usuario in self.usuarios_cadastrados:
            if usuario.nome.lower() == nome.lower():
                usuario_cadastrado = usuario
                break
        
        if usuario_cadastrado is None:
            print("Usuário não cadastrado. Por favor, cadastre-se primeiro.")
            return
        
        novo_livro = Livro(titulo, autor, ano, "Emprestado")
        self.livros_cadastrados.append(novo_livro)

        usuario_cadastrado.emprestados.append(titulo)

        print("Livro cadastrado com sucesso!")
    
    def Interface():
        while True:
            print("--Menu--")
            print("1. Cadastrar Usuário")
            print("2. Cadastrar Livro")
            print("3. Exibir Usuários Cadastrados")
            print("4. Sair")

            escolha = input("Escolha uma das opções: ")

            if escolha == "1":
                biblioteca.adicionarUsuario()
            if escolha == "2":
                biblioteca.adicionarLivro()
            elif escolha == "3":
                biblioteca.exibirUsuarios()
            elif escolha == "4":
                break


            
class Usuario:
    def __init__(self, nome, email, emprestados):
        self.nome = nome
        self.email = email
        self.emprestados = emprestados
    
class Livro:
    def __init__(self, titulo, autor, ano, status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

def Interface():
    while True:
        print("--Menu--")
        print("1. Cadastrar Usuário")
        print("2. Cadastrar Livro")
        print("3. Exibir Usuários Cadastrados")
        print("4. Sair")

        escolha = input("Escolha uma das opções: ")

        if escolha == "1":
            biblioteca.adicionarUsuario()
        if escolha == "2":
            biblioteca.adicionarLivro()
        elif escolha == "3":
            biblioteca.exibirUsuarios()
        elif escolha == "4":
            break

biblioteca = Biblioteca()
biblioteca.Interface()