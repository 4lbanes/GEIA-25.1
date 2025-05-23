
# Esse sistema é um sistema de gerenciamento de biblioteca, onde o usuario pode cadastrar livros, emprestar livros, devolver livros e gerenciar clientes.
# O sistema possui duas classes principais: Livro e Cliente, que herdam de LivroDigital e LivroFisico, respectivamente.
# Ele também possui um menu interativo que permite ao usuario escolher a operação que deseja realizar.
# O sistema possui uma dependencia a 2 arquivos de textos: Livros.txt e Clientes.txt, onde os dados dos livros e clientes são armazenados.

#Na Funcao main() (A qual sera executada no final de cada uma das funcoes presentes dentro funcao menu()) retorna para o menu principal e carrega novamente a lista de livros e clientes
def main():
    Cliente.carregar_clientes()
    Livro.carregar_livros()
    menu()

#Definindo listas globais para armazenar livros e clientes
#Por enquanto, as listas estao vazias, mas elas serao preenchidas com os dados dos arquivos Livros.txt e Clientes.txt

#OBS. Todos os livros e clientes sao ficcionais e foram criados apenas para fins de teste :)
livros = []
clientes = []

#Definindo as classes Livro que sera usada para armazenar os dados do Livros.txt
class Livro:
    def __init__(self, titulo, autor, status, condicao, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.status = status
        self.condicao = condicao
        self.quantidade = quantidade
    #Sistema de Carregar Livros (Carregar os livros do arquivo Livros.txt)
    def carregar_livros():
        try:
            #Abrindo o arquivo Livros.txt e lendo as linhas
            with open('Livros.txt', 'r') as file:
                #Lendo cada linha do arquivo e separando os dados por vírgula
                for linha in file:
                    titulo, autor, status, condicao, quantidade = linha.strip().split(",")
                    #Adicionando os dados do livro a lista de livros
                    livros.append({"titulo": titulo, "Autor": autor, "status": status, "condicao": condicao, "quantidade": quantidade})
                    #Imprimindo para o usuario os dados do livro
                    print(f"Livro: {titulo} | Autor: {autor} | Status: {status} | Condicao: {condicao} | Quantidade: {quantidade} \n")
                print("--------------------------------------------------------------------------------------------------------------------------")
            return livros
        #Se a funcao nao conseguir abrir o arquivo Livros.txt, ela ira imprimir uma mensagem de erro
        except FileNotFoundError:
            print ("Ocorreu algum erro ao carregar os livros.")
            return
# O Livro digital (Que herda a classe Livro) Sempre estara disponivel, portanto sua quantidade sempre sera 1
class LivroDigital(Livro):
    def __init__(self):
        for livro in livros:
            if livros["condicao"] == "Digital":
                livro["status"] = "Disponivel"
# O Livro digital (Que herda a classe Livro) Podera estar Disponivel se a quantidade for maior que 0
#Caso contrario, o livro sera considerado Indisponivel
class LivroFisico(Livro):
    def __init__(self):
        for livro in livros:
            if livro["condicao"] == "Fisico":
                livro_quantidade_int = int(livro['quantidade'])
                if livro_quantidade_int > 0:
                    livro["status"] = "Disponivel"
            else:
                livro["status"] = "Indisponivel"
#Definindo as classes Cliente que sera usada para armazenar os dados do Clientes.txt
class Cliente:  
    def __init__(self, nome_cliente, livros_emprestados, assinatura):
        self.nome_cliente = nome_cliente
        self.livros_emprestados = livros_emprestados
        self.assinatura = assinatura
    #Sistema de Carregar Livros (Carregar os livros do arquivo Livros.txt)         
    def carregar_clientes():
        try:
            #Lendo cada linha do arquivo e separando os dados por vírgula
            with open('Clientes.txt', 'r') as file:
                for linha in file:
                    #Adicionando os dados do livro a lista de livros
                    nome_cliente, livros_emprestados, assinatura, espacos_disponiveis = linha.strip().split("|")
                    clientes.append({"nome_cliente": nome_cliente, "livros_emprestados": livros_emprestados, "assinatura": assinatura, "espacos_disponiveis": espacos_disponiveis})
                    #Se o cliente nao tiver livros emprestados, ele ira imprimir "Nenhum" ao inves de uma string vazia
                    if livros_emprestados == "":
                        livros_emprestados = "Nenhum"
                    #Imprimindo para o usuario os dados do cliente
                    print(f"Cliente: {nome_cliente}| livros emprestados: {livros_emprestados} | Assinatura: {assinatura}| Espacos disponiveis: {espacos_disponiveis}\n")
                print("--------------------------------------------------------------------------------------------------------------------------")
            return clientes
        except FileNotFoundError:
            print ("Ocorreu algum erro ao carregar os clientes.")
            return
#O Cliente VIP (Que herda a classe Cliente) Podera ter ate 5 livros emprestados simutaneamente
class ClienteVIP(Cliente):
    def __init__(self):
        for cliente in clientes:
            if cliente["assinatura"] == "VIP":
                cliente['espacos_disponiveis'] = 5

#O Cliente VIP (Que herda a classe Cliente) Podera ter ate 2 livros emprestados simutaneamente
class ClienteRegular(Cliente):
    def __init__(self):
        for cliente in clientes:
            if cliente["assinatura"] == "Regular":
                cliente['espacos_disponiveis'] = 2

#Sistema de Busca de Livro (Buscar um livro pelo título e retornar o seu status)
def buscar_livro(livros):
    #Input do usuario para buscar o livro
    Busca = input("Digite o nome ou autor(a) do livro: ")
    repeticao = 0
    for livro in livros:
        #Verifica se o livro existe na lista de livros
        #O .lower() serve para evitar conflitos de letras maiusculas e minusculas
        if (livro['titulo'].lower() == Busca.lower() or livro['Autor'].lower() == Busca.lower()) and repeticao == 0:
            #Se o livro for Fisico, ele ira imprimir a quantidade do livro
            #Se o livro for Digital, ele ira imprimir apenas o status do livro
            if livro['condicao'] == "Digital":
                print(f"Livro: {livro['titulo']}, Autor: {livro['Autor']}, Status: {livro['status']} Condicao: {livro['condicao']}\n")
                repeticao += 1
            elif livro['condicao'] == "Fisico":
                print(f"Livro: {livro['titulo']}, Autor: {livro['Autor']}, Status: {livro['status']} Condicao: {livro['condicao']}, Quantidade: {livro['quantidade']}\n")
            #Se o livro nao existir na lista de livros, ele ira imprimir uma mensagem de erro
            else:
                print("Esse livro está indisponivel.")
                #Retornando para a funcao main()
                Continuar = input("Deseja continuar? (S/N): ")
                if Continuar.lower() == "s":
                    main()
            #Imprimindo os clientes que estao emprestando o livro
            with open('Livros.txt', 'r') as file:
                #Olhando linha por linha
                for linha in file:
                    #Separando os dados do livro por ","
                    titulo, autor, status, condicao, quantidade = linha.strip().split(",")
            with open('Clientes.txt', 'r') as file:
                    #inicialmente a lista de clientes que estao emprestando o livro sera vazia
                    clientes_emprestando = []
                    #Analizando linha por linha de clientes
                    for linha in file:
                        #Separando os dados do cliente por "|"
                        nome_cliente, livros_emprestados, assinatura, espacos_disponiveis = linha.strip().split("|")
                        #Analizando os livros emprestados do cliente
                        livros_adquiridos = livros_emprestados.strip().split(",")
                        for livro in livros_adquiridos:
                            #Se o livro que o cliente esta emprestando for igual ao livro que o usuario digitou, ele ira adicionar o cliente a lista de clientes_emprestando
                            #O .lower() serve para evitar conflitos de letras maiusculas e minusculas
                            if livro.lower() == Busca.lower():
                                clientes_emprestando.append(nome_cliente)
                    #Se a lista de clientes_emprestando estiver vazia, ele ira imprimir "Nenhum cliente emprestando"
            #Se o usuario tiver pesquisado pelo autor, o codigo ira imprimir todos os livros pelo mesmo autor
                    if clientes_emprestando == []:
                        print("---------------------------------------------------------------")
                        print("Esse livro não está emprestado por nenhum cliente.")
                        print("---------------------------------------------------------------")
        #imprimindo os clientes que estao emprestando o livro
                    elif autor.lower() != Busca.lower() and clientes_emprestando != []:
                        print("-----------------------------------------------------------------------------------")
                        print(f"Esse livro esta sendo emprestado pelos clientes: {', '.join(clientes_emprestando)}")
                        print("-----------------------------------------------------------------------------------")
    #Retornando para a funcao main()
    Continuar = input("Deseja continuar? (S/N): ")
    if Continuar.lower() == "s":
        main()

def cadastrar_livro(livros):
    #Sistema de Cadastrar Livro (Adicionar um livro e autor ao arquivo Livros.txt)
    #Pegando os dados do livro atraves dos inputs do usuario
    Titulo = input("Digite o título do livro: ")
    Autor = input("Digite o autor do livro: ")
    #O status do livro sera sempre "Disponivel" ja que ele vai ter acabado de ser cadastrado
    Status = " Disponivel"
    Condicao = input("Digite a condicao do livro (Fisico ou Digital): ")
    if Condicao.lower() == "fisico":
        #Reafirmando a condicao como "Fisico", pois se o "Fisico" for escrito de forma diferente 
        #(Com alguma outra letra em maiusculo ou minusculo), o sistema de carregar livros podera quebrar
        Condicao = "Fisico"
        Quantidade = input("Digite a quantidade do livro: ")
        #Se a quantidade for 0, o sistema ira imprimir uma mensagem de erro e o livro sera cadastrado como Digital
        if Quantidade == "0":
            print("A quantidade do livro não pode ser 0. O livro será cadastrado como Digital.")
            Condicao = "Digital"
            Quantidade = 0
        #Se a quantidade for um numero inteiro, o sistema ira imprimir uma mensagem de erro e retonara ao menu
        elif Quantidade == float:
            print("A quantidade do livro tem que ser um numero inteiro.")
            #Retornando para a funcao main()
            Continuar = input("Deseja continuar? (S/N): ")
            if Continuar.lower() == "s":
                main()
    elif Condicao.lower() == "digital":
        #Mesma situacao para o "Digital"
        Condicao = "Digital"
        Quantidade = 0
    #Se o usuario digitar uma condicao diferente de "Fisico" ou "Digital", o sistema ira imprimir uma mensagem de erro
    #E o livro sera cadastrado como "Fisico" por padrao
    else:
        print("Condicao inválida. O livro será cadastrado como Fisico.")
        Condicao = "Fisico"
        Quantidade = input("Digite a quantidade do livro: ")
    livros.append({"titulo": Titulo, "Autor": Autor, "status": Status, "condicao": Condicao, "quantidade": Quantidade})
    #Adicionando os dados do livro ao arquivo Livros.txt
    with open ("livros.txt", "a") as file:
        file.write(f"{Titulo},{Autor},{Status},{Condicao},{Quantidade}\n")
        print(f"Livro {Titulo} cadastrado com sucesso!")
    #Retornando para a funcao main()
    Continuar = input("Deseja continuar? (S/N): ")
    if Continuar.lower() == "s":
        main()

#Sistema de clientes poderem pegar livros emprestados (A maior parte do codigo)
#Resumindo: O usuario digita o nome do livro que deseja pegar emprestado,
#o sistema verifica se o livro existe e se ele esta disponivel, e se estiver, Atualiza o status do livro e do cliente
def emprestar_livro(livros, clientes):
    #Determinando o cliente e o livro que ele deseja pegar emprestado
    cliente_personalizado = input("Digite o seu Email (cliente): \n")
    livro_proucurado = input("Digite o nome do livro que proucura:  \n")
    #Verificando se o livro existe na lista de livros
    for livro in livros:
        #O .lower() serve para evitar conflitos de letras maiusculas e minusculas
        if livro["titulo"].lower() == livro_proucurado.lower():
            #Se o livro existir na lista de livros, ele ira verificar se o livro esta disponivel
            if livro["status"] == "Disponivel":
                #Pegando a resposta do usuario se ele deseja pegar o livro emprestado
                Resposta = input("você deseja emprestar esse livro? (S/N)")
                #Se o usuario digitar "S", o sistema ira verificar se o cliente tem espacos disponiveis
                for cliente in clientes:
                    if cliente['nome_cliente'].lower() == cliente_personalizado.lower():
                        #Definindo o espaco disponivel do cliente como int
                        request_espacos_disponiveis = int(cliente['espacos_disponiveis'])
                if Resposta == "S" and request_espacos_disponiveis > 0:
                    #Se o cliente for pegar o livro emprestado, e o livro for Fisico,
                    #ele ira diminuir a quantidade do livro em 1
                    if livro['condicao'] == "Fisico":
                        quantidade_int = int(livro['quantidade'])
                        quantidade_int -= 1
                    #Atualizando a lista de livros adiquiridos do cliente
                    with open('Clientes.txt', 'r') as file:
                        for linha in file:
                            #Separando os dados do cliente por "|"
                            nome_cliente, livros_emprestados, assinatura, espacos_disponiveis = linha.strip().split("|")
                            #Se o nome do cliente for igual ao nome do cliente que o usuario digitou, ele ira atualizar os dados do cliente
                            if nome_cliente == cliente_personalizado:
                                #Diminuindo o espaco disponivel do cliente em 1
                                espacos_disponiveis = int(espacos_disponiveis)
                                espacos_disponiveis -= 1
                                cliente['espacos_disponiveis'] = espacos_disponiveis
                                #Adicionando o livro emprestado a lista de livros adiquiridos do cliente
                                livros_adquiridos = livros_emprestados.split(",")
                                if livro['titulo'] not in livros_adquiridos:
                                    livros_adquiridos.append(livro['titulo'])
                    with open("Clientes.txt", "w") as file:
                        #Reescrevendo os dados dos clientes restantes no arquivo Clientes.txt
                        for cliente in clientes:
                            if cliente['nome_cliente'] == cliente_personalizado:
                                cliente['livros_emprestados'] = ",".join(livros_adquiridos)
                            file.write(f"{cliente['nome_cliente']}|{cliente['livros_emprestados']}|{cliente['assinatura']}|{str(espacos_disponiveis)}\n")
                    #Reescrevendo os dados dos livros restantes no arquivo Livros.txt
                    with open("livros.txt", "w") as file:
                        for livro in livros:
                            if livro["titulo"].lower() == livro_proucurado.lower():
                                livro['quantidade'] = quantidade_int
                                #Se a quantidade do livro for 0, o status do livro sera "Indisponivel"
                                if livro['quantidade'] == 0:
                                    livro['status'] = "Indisponivel"
                            file.write(f"{livro['titulo']},{livro['Autor']},{livro['status']},{livro['condicao']},{livro['quantidade']}\n")
                    #Imprimindo a mensagem de sucesso
                    print("Livro emprestado com sucesso!")
                    #Retornando para a funcao main()
                    Continuar = input("Deseja continuar? (S/N): ")
                    if Continuar.lower() == "s":
                        main()
                #Se o cliente nao tiver espacos disponiveis, o sistema ira imprimir uma mensagem de erro
                else:
                    print("Você não tem mais espaços disponíveis.")
                    #Retornando para a funcao main()
                    Continuar = input("Deseja continuar? (S/N): ")
                    if Continuar.lower() == "s":
                        main()
            #Se o livro nao estiver disponivel, o sistema ira imprimir uma mensagem de erro
            else:
                print("Esse livro está indisponível.")
                #Retornando para a funcao main()
                Continuar = input("Deseja continuar? (S/N): ")
                if Continuar.lower() == "s":
                    main()
    return

#Sistema de clientes devolverem livros
def devolver_livro(livros, clientes):
    #Determinando o cliente que deseja devolver o livro
    cliente_personalizado = input("Digite o seu Email (cliente): ")
    #Determinando o livro que o cliente deseja devolver
    for livro in livros:
        with open('Clientes.txt', 'r') as file:
            for linha in file:
                nome_cliente, livros_emprestados, assinatura, espacos_disponiveis = linha.strip().split("|")
                if nome_cliente == cliente_personalizado:
                    print(f"Livros emprestados: {livros_emprestados}")
                    livros_adquiridos = livros_emprestados.strip().split(",")
                    #Caso o cliente nao tenha livros emprestados, ele ira imprimir a mensagem de erro "Nenhum livro emprestado" e voltara para a funcao main()
                    if livros_adquiridos == [""]:
                        print("Nenhum livro emprestado.")
                        #Retornando para a funcao main()
                        Continuar = input("Deseja continuar? (S/N): ")
                        if Continuar.lower() == "s":
                            main()
                    #Escolhendo o livro que o cliente deseja devolver
                    livro_devolver = input("Digite o nome do livro que deseja devolver: ")
                    #Verificando se o livro existe na lista de livros emprestados
                    for livro in livros_adquiridos:
                        #Se o livro existir na lista de livros emprestados, ele ira remover o livro da lista de livros emprestados
                        if livro.lower() == livro_devolver.lower():
                            livros_adquiridos.remove(livro)
                            #Adicionando de volta +1 na quantidade do espacos disponiveis
                            espacos_disponiveis = int(espacos_disponiveis) + 1
                            #Adicionando o livro devolvido de volta a lista de livros
                            with open("Clientes.txt", "w") as file:
                                #Reescrevendo os dados dos clientes restantes no arquivo Clientes.txt
                                for cliente in clientes:
                                    #Se o cliente for o mesmo que o cliente que deseja devolver o livro, ele ira atualizar os dados do cliente
                                    if cliente['nome_cliente'] == cliente_personalizado:
                                        cliente['livros_emprestados'] = ",".join(livros_adquiridos)
                                        cliente['espacos_disponiveis'] = espacos_disponiveis
                                    #OBS. Ja que o cliente foi adcionado de volta a Clientes.txt, nao e necessario utilizar o .append por enquanto,
                                    #ja que o codigo vai retornar para a funcao main() e recarregar a lista
                                    file.write(f"{cliente['nome_cliente']}|{cliente['livros_emprestados']}|{cliente['assinatura']}|{cliente['espacos_disponiveis']}\n")
                                    
                        with open("livros.txt", "w") as file:
                            for livro in livros:
                                #Proucurando o livro recem devolvido na lista de livros
                                if livro["titulo"].lower() == livro_devolver.lower():
                                    #Se o livro for Fisico, ele ira adicionar +1 na quantidade do livro
                                    if livro['condicao'] == "Fisico":
                                        quantidade_int = int(livro['quantidade'])
                                        quantidade_int += 1
                                        livro['quantidade'] = quantidade_int
                                        #Se a quantidade do livro for maior que 0, o status do livro sera "Disponivel"
                                        if livro['quantidade'] > 0:
                                            livro['status'] = "Disponivel"
                                        #Reescrevendo os dados dos livros restantes no arquivo Livros.txt
                                    for livro in livros:
                                        #OBS. Ja que o livro foi adcionado de volta a Livros.txt, nao e necessario utilizar o .append por enquanto,
                                        #ja que o codigo vai retornar para a funcao main() e recarregar a lista
                                        file.write(f"{livro['titulo']},{livro['Autor']},{livro['status']},{livro['condicao']},{livro['quantidade']}\n")
                        #Retornando para a funcao main()
                        Continuar = input("Deseja continuar? (S/N): ")
                        if Continuar.lower() == "s":
                            main()
                    #Se o livro nao existir na lista de livros emprestados, ele ira imprimir a mensagem de erro "Esse livro não está emprestado"
                    else:
                        print("Esse livro não está emprestado.")
                        #Retornando para a funcao main()
                        Continuar = input("Deseja continuar? (S/N): ")
                        if Continuar.lower() == "s":
                            main()
    return

            
#Sistema de Gerenciar Clientes (Cadastrar, ver informacoes e ate remover cliente)
def gerenciar_clientes(clientes):
    #Mostrando as opcoes para o usuario
    print("1. Gerenciar clientes")
    print("2. Cadastrar cliente")
    print("3. Remover cliente")
    print("--------------------------------")
    #Pegando a opcao do usuario
    operacao_cliente = input("Qual operação deseja realizar?\n")
    if operacao_cliente == "1":
        #Mostrando os clientes cadastrados
        #Lendo o arquivo Clientes.txt
        with open('Clientes.txt', 'r') as file:
            #Olhando linha por linha
            for linha in file:
                #separando os dados por "|"
                nome_cliente, livros_emprestados, assinatura, espacos_disponiveis = linha.strip().split("|")
                #Caso o cliente nao tenha livros emprestados, ele ira imprimir "Nenhum" ao inves de uma string vazia
                if livros_emprestados == "":
                    livros_emprestados = "Nenhum"
                #Adicionando os dados do cliente a lista de clientes
                clientes.append({"nome_cliente": nome_cliente, "livros_emprestados": livros_emprestados,  "assinatura": assinatura, "espacos_disponiveis": espacos_disponiveis})
                #Imprimindo os dados dos clientes
                print(f"Cliente: {nome_cliente}| livros emprestados: {livros_emprestados} | Assinatura: {assinatura}| Espacos disponiveis: {espacos_disponiveis}\n")
                #Retornando para a funcao main()
                Continuar = input("Deseja continuar? (S/N): ")
                if Continuar.lower() == "s":
                    main()
        return clientes
    elif operacao_cliente == "2":
        #Pegando os dados do cliente atraves dos inputs do usuario
        #O nome do cliente sera o email dele
        nome_cliente = input("Digite o seu Email (cliente): ")
        livros_emprestados = ""
        assinatura = input("Digite o tipo de assinatura (VIP ou Regular): ")
        #Se o usuario escolher a assinatura VIP, ele tera 5 espacos de livros disponiveis
        #Se o usuario escolher a assinatura Regular, ele tera 2 espacos de livros disponiveis
        if assinatura.lower() == "vip":
            espacos_disponiveis = 5
        elif assinatura.lower() == "regular":
            espacos_disponiveis = 2
        #Se o usuario digitar uma assinatura diferente de "VIP" ou "Regular", o sistema ira imprimir uma mensagem de erro
        else:
            print("Assinatura inválida.")
            #Retornando para a funcao main()
            Continuar = input("Deseja continuar? (S/N): ")
            if Continuar.lower() == "s":
                main()
        #Adicionando os dados do cliente a lista de clientes
        clientes.append({"nome_cliente": nome_cliente, "livros_emprestados": livros_emprestados, "assinatura": assinatura, "espacos_disponiveis": espacos_disponiveis})
        #Adicionando os dados do cliente ao arquivo Clientes.txt
        with open("Clientes.txt", "a") as file:
            file.write(f"{nome_cliente}|{livros_emprestados}|{assinatura}|{str(espacos_disponiveis)}\n")
            #Imprimindo a mensagem de sucesso
            print(f"Cliente {nome_cliente} cadastrado com sucesso!")
            #Retornando para a funcao main()
            Continuar = input("Deseja continuar? (S/N): ")
            if Continuar.lower() == "s":
                main()
    elif operacao_cliente == "3":
        #Pegando o nome do cliente atraves do input do usuario
        nome_cliente = input("Digite o nome do cliente que deseja remover: ")
        #Analisando cliente por cliente da lista de clientes
        for cliente in clientes:
            #Se o nome do cliente for igual ao nome do cliente que o usuario digitou, ele ira remover o cliente da lista
            if cliente['nome_cliente'] == nome_cliente:
                clientes.remove(cliente)
                #Removendo o cliente do arquivo Clientes.txt
                with open("Clientes.txt", "w") as file:
                    #Reescrevendo os dados dos clientes restantes no arquivo Clientes.txt
                    for cliente in clientes:
                        file.write(f"{cliente['nome_cliente']}|{cliente['livros_emprestados']}|{cliente['assinatura']}|{str(cliente['espacos_disponiveis'])}\n")
                    #Imprimindo a mensagem de sucesso
                print(f"Cliente {nome_cliente} removido com sucesso!")
                #Retornando para a funcao main()
                Continuar = input("Deseja continuar? (S/N): ")
                if Continuar.lower() == "s":
                    main()
    #Se o usuario digitar uma operacao diferente de "1", "2" ou "3", o sistema ira imprimir uma mensagem de erro
    else:
        print("Operação inválida. Tente novamente.")
        #Retornando para a funcao main()
        Continuar = input("Deseja continuar? (S/N): ")
        if Continuar.lower() == "s":
            main()
    
#Sistema de Menu (Menu principal do sistema)
def menu():
    #Mostrando as opcoes para o usuario
    print("1. Buscar Livro")
    print("2. Cadastrar livro")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Gerenciar clientes")
    print("6. Sair")
    #Pegando a opcao do usuario
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        buscar_livro(livros)
    elif opcao == 2:
        cadastrar_livro(livros)
    elif opcao == 3:
        emprestar_livro(livros, clientes)
    elif opcao == 4:
        devolver_livro(livros, clientes)
    elif opcao == 5:
        gerenciar_clientes(clientes)
    elif opcao == 6:
        print("Saindo...")
        return
    #Se o usuario digitar uma opcao diferente de "1", "2", "3", "4", "5" ou "6", o sistema ira imprimir uma mensagem de erro
    else:
        print("Opção inválida. Tente novamente.")

main()