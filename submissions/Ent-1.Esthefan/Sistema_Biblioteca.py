from abc import ABC, abstractmethod

class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar(self, dado):
        novo = No(dado)
        if not self.inicio:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo

    def buscar(self, condicao):
        atual = self.inicio
        resultados = []
        while atual:
            if condicao(atual.dado):
                resultados.append(atual.dado)
            atual = atual.proximo
        return resultados

    def iterar(self):
        atual = self.inicio
        while atual:
            yield atual.dado
            atual = atual.proximo

class Livro(ABC):
    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._emprestado = False

    @abstractmethod
    def exibir_detalhes(self):
        pass

    def esta_disponivel(self):
        return not self._emprestado

    def emprestar(self):
        if not self._emprestado:
            self._emprestado = True
            return True
        return False

    def devolver(self):
        if self._emprestado:
            self._emprestado = False
            return True
        return False

    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_status(self):
        return "Emprestado" if self._emprestado else "Disponível"

class Usuario(ABC):
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._livros_emprestados = []

    def get_email(self):
        return self._email

    def get_nome(self):
        return self._nome

    def adicionar_livro(self, livro):
        self._livros_emprestados.append(livro)

    def remover_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)

    def listar_livros(self):
        return self._livros_emprestados

    @abstractmethod
    def pode_emprestar(self):
        pass

# Livros

class LivroFisico(Livro):
    def __init__(self, titulo, autor, ano, local):
        super().__init__(titulo, autor, ano)
        self._local = local

    def exibir_detalhes(self):
        return f"[Físico] {self._titulo} - {self._autor} ({self._ano}) | Local: {self._local} | Status: {self.get_status()}"

    def get_local(self):
        return self._local

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano, url):
        super().__init__(titulo, autor, ano)
        self._url = url

    def exibir_detalhes(self):
        return f"[Digital] {self._titulo} - {self._autor} ({self._ano}) | URL: {self._url} | Livre acesso"

    def emprestar(self):
        return False  # Livros digitais não são emprestados

    def devolver(self):
        return False

# Usuarios

class UsuarioRegular(Usuario):
    def pode_emprestar(self):
        return len(self._livros_emprestados) < 3

class UsuarioVIP(Usuario):
    def pode_emprestar(self):
        return len(self._livros_emprestados) < 10

# Biblioteca

class Biblioteca:
    def __init__(self):
        self.livros = ListaEncadeada()
        self.usuarios = ListaEncadeada()

    def cadastrar_livro(self, livro):
        self.livros.adicionar(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.adicionar(usuario)

    def buscar_usuario_por_email(self, email):
        usuarios = self.usuarios.buscar(lambda u: u.get_email() == email)
        return usuarios[0] if usuarios else None

    def buscar_livros(self, termo):
        resultados = self.livros.buscar(lambda l: termo.lower() in l.get_titulo().lower() or termo.lower() in l.get_autor().lower())
        return resultados

    def emprestar_livro(self, titulo, email):
        usuario = self.buscar_usuario_por_email(email)
        if not usuario:
            print("Usuário não encontrado.")
            return
        livros = self.buscar_livros(titulo)
        for livro in livros:
            if isinstance(livro, LivroFisico) and livro.esta_disponivel():
                if usuario.pode_emprestar():
                    if livro.emprestar():
                        usuario.adicionar_livro(livro)
                        print("Livro emprestado com sucesso!")
                    else:
                        print("Livro não pôde ser emprestado.")
                else:
                    print("Usuário atingiu o limite de empréstimos.")
                return
        print("Livro físico disponível não encontrado.")

    def devolver_livro(self, titulo, email):
        usuario = self.buscar_usuario_por_email(email)
        if not usuario:
            print("Usuário não encontrado.")
            return
        for livro in usuario.listar_livros():
            if livro.get_titulo().lower() == titulo.lower():
                if livro.devolver():
                    usuario.remover_livro(livro)
                    print("Livro devolvido com sucesso!")
                    return
        print("Livro não encontrado na lista de empréstimos do usuário.")

    def relatorio_livros_emprestados(self):
        encontrou = False
        for usuario in self.usuarios.iterar():
            for livro in usuario.listar_livros():
                if isinstance(livro, LivroFisico):
                    encontrou = True
                    print(f"{livro.get_titulo()} - {livro.get_autor()} ({livro.get_status()}) -> Emprestado por: {usuario.get_nome()} ({usuario.get_email()})")
        if not encontrou:
            print("Nenhum livro físico está emprestado no momento.")

    def relatorio_livros(self):
        tem_livros = False
        for livro in self.livros.iterar():
            print(livro.exibir_detalhes())
            tem_livros = True
        if not tem_livros:
            print("Nenhum livro cadastrado.")

    def relatorio_usuarios(self):
        tem_usuario = False
        for usuario in self.usuarios.iterar():
            print(f"{usuario.get_nome()} - {usuario.get_email()}")
            tem_usuario = True
        if not tem_usuario:
            print("Nenhum usuário cadastrado.")

# Menu

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n--- Menu Biblioteca ---")
        print("1. Cadastrar Livro")
        print("2. Cadastrar Usuário")
        print("3. Buscar Livro")
        print("4. Emprestar Livro")
        print("5. Devolver Livro")
        print("6. Relatório de Livros")
        print("7. Relatório de Usuários")
        print("8. Relatório de Livros Emprestados")
        print("9. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tipo = input("Tipo (F - Físico / D - Digital): ").upper()
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            if tipo == "F":
                local = input("Local de acesso: ")
                livro = LivroFisico(titulo, autor, ano, local)
            elif tipo == "D":
                url = input("URL do livro: ")
                livro = LivroDigital(titulo, autor, ano, url)
            else:
                print("Tipo inválido.")
                continue
            biblioteca.cadastrar_livro(livro)
            print("Livro cadastrado com sucesso.")

        elif opcao == "2":
            tipo = input("Tipo (R - Regular / V - VIP): ").upper()
            nome = input("Nome: ")
            email = input("E-mail: ")
            if tipo == "R":
                usuario = UsuarioRegular(nome, email)
            elif tipo == "V":
                usuario = UsuarioVIP(nome, email)
            else:
                print("Tipo inválido.")
                continue
            biblioteca.cadastrar_usuario(usuario)
            print("Usuário cadastrado com sucesso.")

        elif opcao == "3":
            termo = input("Digite o título ou autor para buscar: ")
            resultados = biblioteca.buscar_livros(termo)
            if resultados:
                for livro in resultados:
                    print(livro.exibir_detalhes())
            else:
                print("Nenhum livro encontrado.")

        elif opcao == "4":
            titulo = input("Título do livro: ")
            email = input("E-mail do usuário: ")
            biblioteca.emprestar_livro(titulo, email)

        elif opcao == "5":
            titulo = input("Título do livro: ")
            email = input("E-mail do usuário: ")
            biblioteca.devolver_livro(titulo, email)

        elif opcao == "6":
            biblioteca.relatorio_livros()

        elif opcao == "7":
            biblioteca.relatorio_usuarios()

        elif opcao == "8":
            biblioteca.relatorio_livros_emprestados()

        elif opcao == "9":
            print("Você Saiu do Sistema ")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
