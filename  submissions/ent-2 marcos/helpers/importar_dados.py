import csv
from helpers.analise_estatistica import AnaliseEstatistica
from helpers.deteccao_outliers import DeteccaoOutliers

class ImportarDados:
    def __init__(self, path):
        self.path = path # Caminho do arquivo CSV
        self.header = [] # Cria uma lista vazia para armazenar os nomes das colunas, ou seja primeira linha...
        self.dados = [] # Cria uma lista vazia onde serao armazenados os dados do CSV
        self.importar() # Aqui é pra ele chamar essa função assim que for criado

    def importar(self):
        with open(self.path, newline='') as csvfile:
            leitor = csv.reader(csvfile, delimiter=',')
            self.header = next(leitor) # Next é usado para ler a primeira linha do CSV, que contém os nomes das colunas
            for linha in leitor: # Aqui ele continua a partir da segunda linha, e guarda na lista...
                self.dados.append(linha)

    def get_coluna(self, nome_coluna):
        # Pega o índice da coluna pelo nome e retorna uma lista com os valores convertidos para float
        idx = self.header.index(nome_coluna)
        return [float(linha[idx]) for linha in self.dados]

    def mostrar_relatorio(self):
        colunas_numericas = ["Idade", "Nota_Matematica", "Nota_Estatistica", "Nota_Programacao", "Faltas"]

        print("\n--- Análise Estatística ---")
        for coluna in colunas_numericas:
            valores = self.get_coluna(coluna) # Pega os valores daquela coluna
            estat = AnaliseEstatistica(valores) # Cria o objeto para calcular as estatísticas
            print(f"\nColuna: {coluna}")
            print(f"Média: {estat.media():.2f}") # Mostra a média
            print(f"Moda: {estat.mode():.2f}") # Mostra a moda
            print(f"Mediana: {estat.median():.2f}") # Mostra a mediana
            print(f"Desvio Padrão: {estat.std():.2f}") # Mostra o desvio padrão
            print(f"Variância: {estat.variance():.2f}") # Mostra a variância
            print(f"Intervalo: {estat.interval()}") # Mostra o intervalo (menor e maior valor)

        print("\n--- Detecção de Outliers ---")
        for coluna in ["Nota_Matematica", "Nota_Estatistica", "Nota_Programacao", "Faltas"]:
            valores = self.get_coluna(coluna) # Pega os valores daquela coluna
            outlier = DeteccaoOutliers(valores) # Cria o objeto para detectar outliers
            idx_zscore = outlier.zscore() # Pega os índices dos outliers pelo Z-Score
            idx_tukey = outlier.cerca_tukey() # Pega os índices dos outliers pela Cerca de Tukey
            print(f"\nColuna: {coluna}")
            print(f"Outliers Z-Score (índices): {list(idx_zscore)}") # Mostra os índices dos outliers pelo Z-Score
            print(f"Outliers Tukey (índices): {list(idx_tukey)}") # Mostra os índices dos outliers pela Cerca de Tukey
            ids_zscore = [self.dados[i][0] for i in idx_zscore] # Pega o ID do aluno para cada índice de outlier Z-Score
            ids_tukey = [self.dados[i][0] for i in idx_tukey] # Pega o ID do aluno para cada índice de outlier Tukey
            print(f"IDs Outliers Z-Score: {ids_zscore}") # Mostra os IDs dos outliers pelo Z-Score
            print(f"IDs Outliers Tukey: {ids_tukey}") # Mostra os IDs dos outliers pela Cerca de Tukey