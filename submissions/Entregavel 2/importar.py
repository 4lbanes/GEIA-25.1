import csv
import numpy as np

class ImportarDados():
    def __init__(self, caminho_arquivo):
        self.caminho = caminho_arquivo
        self.dados_numericos = []
        self.ids = []

    def importar(self):
        with open(self.caminho, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.ids.append(row['ID'])
                self.dados_numericos.append([
                    float(row['Idade']),
                    float(row['Nota_Matematica']),
                    float(row['Nota_Estatistica']),
                    float(row['Nota_Programacao']),
                    float(row['Faltas'])
                ])
        return np.array(self.dados_numericos), self.ids