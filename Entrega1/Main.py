from Biblioteca import Biblioteca

biblioteca = Biblioteca()
while(True):
    print("\nO que deseja fazer?")
    print("1. Cadastrar livro ou usuário?")
    print("2. Buscar livro ou usuário?")
    print("3. Alugar livro?")
    print("4. Devolver livro?")
    print("5. Ver relatório dos livro emprestados?")
    print("0. Sair")
    ans = int(input("\nDigite o número da sua ação: "))

    match(ans):
        case 1:
            print("\n1. Livro")
            print("2. Usuário")
            biblioteca.cadastrar(int(input("\nQual deseja cadastrar? ")))
        case 2:
            print("\n1. Livro")
            print("2. Usuário")
            biblioteca.buscar(int(input("\nQual deseja buscar? ")))
        case 3:
            biblioteca.emprestar(input("\nDigite seu nome: "), input("Digite o nome do livro que deseja alugar: "))
        case 4:
            biblioteca.devolver(input("\nDigite seu nome: "), input("Digite o nome do livro que deseja devolver: "))
        case 5:
            biblioteca.relatorio()
        case 0:
            print("Programa finalizado")
            break