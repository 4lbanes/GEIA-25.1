from helpers.importar_dados import ImportarDados

def main():
    caminho_csv = "data/base_ent2.csv"
    dados = ImportarDados(caminho_csv)
    dados.mostrar_relatorio()

if __name__ == "__main__":
    main()