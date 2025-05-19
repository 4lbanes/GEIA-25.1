class ImportarDados():
    def __init__(self, caminho_arquivo):
        self.caminho = caminho_arquivo
        self.dados = None

    def importar(self):
        self.dados = pd.read_csv(self.caminho)
        return self.dados