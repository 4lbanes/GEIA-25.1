import numpy as np

class ImportarDados():
    def __init__(self, caminho_arquivo):
        self.caminho = caminho_arquivo
        self.dados = None

    def importar(self):
        self.dados = np.loadtxt(self.caminho, delimiter=',', skiprows=1)
        return self.dados