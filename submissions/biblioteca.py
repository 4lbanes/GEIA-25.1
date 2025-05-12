from livro import LivroFisico, LivroDigital 
from usuario import UsuarioRegular, UsuarioVIP

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self):
        ''' A função a seguir faz o cadastro de um novo livro usando os inputs do usuario para definir os valores do mesmo, em seguida adiciona o livro à coleção (self.livros) e confirma o cadastro, o livro é criado com base no tipo informado (fisico/digital) e assume comportamentos diferentes.'''
        print("--- Cadastro de livros ---")
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano de publicação: ")
        while True:
            tipo = input("Tipo do livro (fisico/digital): ").lower()
            if tipo in ["fisico", "digital"]:
                break
            print("Tipo inválido! Escolha entre 'fisico' ou 'digital'!")

        if tipo == "fisico":
            novo_livro = LivroFisico(titulo, autor, ano)
        else:
            novo_livro = LivroDigital(titulo, autor, ano)

        self.livros.append(novo_livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")
        

    def remover_livro(self):
        '''Função para remover os livros da lista interna, usando um for loop, o titulo do livro é usado como palavra chave para encontrar o objeto correto para remover'''
        print("--- Remoção de livros ---")
        titulo = input("Digite o título do livro a ser removido: ")
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                self.livros.remove(livro)
                print(f"Livro '{titulo}' removido com sucesso!")
                return
            
        print(f"Nenhum livro com o título '{titulo}' foi encontrado.")

    def cadastrar_usuario(self):
        '''Função que realiza o cadastro do usuario, semelhante à função de cadastro de livro, ela busca um tipo de usuario especifico por meio do while para modificar o objeto criado. O objeto novo então é armazenado na lista interna (self.usuarios)'''
        print("--- Cadastro de Usuário ---")
        nome = input("Nome: ")
        email = input("Email: ")

        while True:
            tipo = input("Tipo de usuário (regular/vip): ").lower()
            if tipo in ["regular", "vip"]:
                break
            print("Tipo inválido! Escolha entre 'regular' ou 'vip'.")

        if tipo == "regular":
            novo_usuario = UsuarioRegular(nome, email)
        else:
            novo_usuario = UsuarioVIP(nome, email)

        self.usuarios.append(novo_usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso como {tipo}!")
        
    def remover_usuario(self):
        '''Remove o usuario com base no nome e no email fornecido via input, verifica se há um match e remove o usuario da lista interna'''
        print("--- Remoção de Usuário ---")
        nome = input("Digite o nome do usuário a ser removido: ")
        email = input("Digite o email do usuário a ser removido: ")
        for usuario in self.usuarios:
            if usuario.nome.lower() == nome.lower() and usuario.email.lower() == email.lower():
                self.usuarios.remove(usuario)
                print(f"Usuário '{nome}' removido com sucesso!")
                return
            
        print("Nenhum usuário encontrado com esse nome e/ou email.")

    def buscar_livro(self, busca):
        '''Realiza uma busca na lista interna por meio de um loop for, esse loop é alimentado com uma palavra-chave(busca) que é fornecida por input, caso o for encontre alguma semelhança dentro da lista interna, por exemplo, a palavra-chave é Um, a função retornaria todos os matches, caso o nome de um autor contesse (u, m), e o mesmo se aplica aos titulos de livros cadastrados.'''
        print("--- Buscar Livro ---")
        pesquisa = [livro for livro in self.livros if busca.lower() in livro.titulo.lower() or busca.lower() in livro.autor.lower()]
        if pesquisa:
            print("Exemplares encontrados:")
            for livro in pesquisa:
                print(livro)
        else:
            print("Nenhum livro encontrado.")

 
    def listar_livros(self):
        '''A função lista todos os livros cadastrados na lista interna (self.livros)'''
        print("--- Listar Livros ---")
        lista = [livro for livro in self.livros]
        if lista:
            print("Livros da coleção: ")
            for livro in lista:
                print(livro)
        else:
            print("Nenhum livro cadastrado")

    def emprestar_livro(self, email, titulo):
        #'''Função responsavel pelo emprestimo de livros, leva como parametros o email do usuario e o titulo do livro, realiza uma busca por ambos nas listas internas, buscando o usuario pelo email cadastrado e o livro pelo titulo, em seguida verifica a disponibilidade do livro e então identifica a subclasse usando isinstance(LivroFisico/Livro Digital) e por fim usa um metodo do usuario para armazenar o livro na lista correta (livros_emprestados para livros fisicos e a variavel booleana livro_digital para livros digitais.)'''
        print("--- Alugar Livro ---")

        usuario = next((usuario for usuario in self.usuarios if usuario.email.lower() == email.lower()), None)
        if not usuario:
            print(f"Usuário com o email '{email}' não encontrado.")
            return

        livro = next((livro for livro in self.livros if livro.titulo.lower() == titulo.lower()), None)
        if not livro:
            print(f"Livro com o título '{titulo}' não encontrado.")
            return

        if not livro.status:
            print(f"O livro '{titulo}' já está emprestado.")
            return

        if isinstance(livro, LivroFisico):
            if len(usuario.livros_emprestados) >= usuario.limite_aluguel():
                print(f"Usuário '{usuario.nome}' atingiu o limite de {usuario.limite_aluguel()} livros físicos.")
                return

        elif isinstance(livro, LivroDigital):
            if usuario.livro_digital is not None:
                print(f"Usuário '{usuario.nome}' já possui um livro digital emprestado.")
                return

        usuario.pegar(livro)
        livro.status = False
        print(f"Livro '{titulo}' emprestado com sucesso para '{usuario.nome}'.")
        
    def devolver_livro(self, email, titulo):
        '''Realiza a devolução de um livro por parte de um usuário, uma busca pelo usuário via o atributo email, então, outra busca pelo livro via o atributo título, identifica a antureza do objeto via isinstance e por fim finaliza a devolução''' 
        print("--- Devolver Livro ---")

        usuario = next((usuario for usuario in self.usuarios if usuario.email.lower() == email.lower()), None)
        if not usuario:
            print(f"Usuário com o email '{email}' não encontrado.")
            return

        livro = next((livro for livro in self.livros if livro.titulo.lower() == titulo.lower()), None)
        if not livro:
            print(f"Livro com o título '{titulo}' não encontrado.")
            return

        if isinstance(livro, LivroFisico):
            if livro not in usuario.livros_emprestados:
                print(f"O livro '{titulo}' não está emprestado para o usuário '{usuario.nome}'.")
                return

        elif isinstance(livro, LivroDigital):
            if usuario.livro_digital != livro:
                print(f"O livro '{titulo}' não está emprestado como livro digital para o usuário '{usuario.nome}'.")
                return

        usuario.devolver(livro)
        livro.status = True
        print(f"Livro '{titulo}' devolvido com sucesso por '{usuario.nome}'.")

    def relatorio(self):
        '''A função relatorio confere primeiro o status dos livros, com "any" e então, caso nenhum livro esteja alugado no momento da geração do relatório (todos os livro.status = True), ele retorna com uma mensagem destacando a disponibilidade, caso exista algum livro emprestado (qualquer livro.status = False), o laço de for procura identificar a classe do livro com isinstance, e retorna uma mensagem personalizada pra tipos diferentes de livro. '''
        print("--- Relatorio de Livros Emprestados ---")
        if not any(not livro.status for livro in self.livros):
            print("Todos os livros estão disponíveis na biblioteca!")
            return
        
        for livro in self.livros:
            if not livro.status:
                for usuario in self.usuarios:
                    if isinstance(livro, LivroFisico) and livro in usuario.livros_emprestados:
                        print(f"O livro físico: {livro.titulo} está em posse do usuario '{usuario.nome}'.")
                    elif isinstance(livro, LivroDigital) and usuario.livro_digital == livro:
                        print(f"O usuario '{usuario.nome}' está em posse de uma cópia digital do livro: '{livro.titulo}'.")