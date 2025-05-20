import numpy as np

class ImportarDados:
    def __init__(self, caminho_arquivo):
        self.array = np.genfromtxt(caminho_arquivo, delimiter=",", skip_header=1)
        self.idade = self.array[:, 1]
        self.mat = self.array[:, 2]
        self.est = self.array[:, 3]
        self.prog = self.array[:, 4]
        self.faltas = self.array[:, 5]

        self.variaveis = {
            'Idade': self.idade,
            'Notas de Matemática': self.mat,
            'Notas de Estatística': self.est,
            'Notas de Programação': self.prog,
            'Faltas': self.faltas
        }

class AnaliseEstatistica:
    def mean(self, array):
        return np.mean(array)

    def median(self, array):
        return np.median(array)

    def mode(self, array):
        valores, counts = np.unique(array, return_counts=True)
        indice_max = np.argmax(counts)
        return valores[indice_max]

    def std(self, array):
        return np.std(array)

    def variance(self, array):
        return np.var(array)

    def interval(self, array):
        return np.max(array) - np.min(array)

    def z_score(self, array):
        return (array - np.mean(array)) / np.std(array)

class DeteccaoOutliers:
    def cerca_turkey(self, array):
        q1 = np.percentile(array, 25)
        q3 = np.percentile(array, 75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        return limite_inferior, limite_superior

    def outliers_tukey(self, array):
        li, ls = self.cerca_turkey(array)
        return array[(array < li) | (array > ls)]

    def outliers_z_score(self, array, limite=3):
        z = (array - np.mean(array)) / np.std(array)
        return array[(z < -limite) | (z > limite)]

dados = ImportarDados("base.csv")
analise = AnaliseEstatistica()
outlier = DeteccaoOutliers()

def generate_report():
    print("Relatório\n")

    for nome, var in dados.variaveis.items():
        print(f"--- {nome} ---")
        print(f"Média: {analise.mean(var):.2f}")
        print(f"Mediana: {analise.median(var):.2f}")
        print(f"Moda: {analise.mode(var)}")
        print(f"Desvio Padrão: {analise.std(var):.2f}")
        print(f"Variância: {analise.variance(var):.2f}")
        print(f"Intervalo: {analise.interval(var):.2f}")
        print(f"Z-Score (amostragem): {np.round(analise.z_score(var), 2)}")

        inf, sup = outlier.cerca_turkey(var)
        print(f"Cerca de Tukey: Inferior = {inf:.2f}, Superior = {sup:.2f}")

        outliers_tukey = outlier.outliers_tukey(var)
        outliers_z = outlier.outliers_z_score(var)

        print(f"Outliers (Tukey): {outliers_tukey}")
        print(f"Outliers (Z-Score): {outliers_z}")
        print()

generate_report()