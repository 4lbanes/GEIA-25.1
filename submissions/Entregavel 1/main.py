from biblioteca import Biblioteca

class Menu:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def interface(self):
        print("\n--Sistema de Administração da Biblioteca--")
        print("1. Cadastrar livro")
        print("2. Remover livro")
        print("3. Cadastrar usuário")
        print("4. Remover usuário")
        print("5. Buscar livro")
        print("6. Listar livros")
        print("7. Alugar livro")
        print("8. Devolver livro")
        print("9. Relatório de livros emprestados")
        print("0. Sair")

class Menu:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def interface(self):
        print("\n--Sistema de Administração da Biblioteca--")
        print("1. Cadastrar livro")
        print("2. Remover livro")
        print("3. Cadastrar usuário")
        print("4. Remover usuário")
        print("5. Buscar livro")
        print("6. Listar livros")
        print("7. Alugar livro")
        print("8. Devolver livro")
        print("9. Relatório de livros emprestados")
        print("0. Sair")

    def terminal(self):
        while True:
            self.interface()
            '''Lê a escolha do usuário e garante que a entrada seja válida'''
            escolha = input("Escolha uma opção: ")
            match escolha:
                case '1':
                    self.biblioteca.cadastrar_livro()
                
                case '2':
                    self.biblioteca.remover_livro()
                
                case '3':
                    self.biblioteca.cadastrar_usuario()
                
                case '4':
                    self.biblioteca.remover_usuario()
                
                case '5':
                    busca = input("Digite um termo para a busca (título/autor): ")
                    self.biblioteca.buscar_livro(busca)
                
                case '6':
                    self.biblioteca.listar_livros()
                
                case '7':
                    email = input("Digite o email do usuario: ")
                    titulo = input("Digite o titulo do livro: ")
                    self.biblioteca.emprestar_livro(email, titulo)
                
                case '8':
                    email = input("Digite o email do usuario: ")
                    titulo = input("Digite o titulo do livro: ")
                    self.biblioteca.devolver_livro(email, titulo)
                
                case '9':
                    self.biblioteca.relatorio()
                
                case '0':
                    print("Encerrando o sistema...")
                    print("...")
                    print("...")
                    break
                case default:
                    print("Tipo inválido! Por favor escolha um digito do menu.")
                    
if __name__ == "__main__":
    app = Menu()
    app.terminal()