import numpy as np

class AnaliseEstatistica():
    def mean(array):
        mean = np.mean(array)
        return mean 
    
    def mode(array):
        valores_unicos, contagens = np.unique(array, return_counts=True)
        max_count = np.max(contagens)
        modas = valores_unicos[contagens == max_count]
        if len(modas) == 1:
            return modas[0]
        return modas.tolist()

    def median(array):
        median = np.median(array)
        return median
    
    def std(array):
        std = np.std(array)
        return std 
    
    def interval(array):
        interval = np.max(array) - np.min(array)
        return interval
    
    def variance(array):
        variance = np.var(array)
        return variance
    
    def generate_report(dados, ids, colunas):
        from outliers import DeteccaoOutliers

        print("\n-- Relatório --")
        for i, nome_coluna in enumerate(colunas):
            col = dados[:, i]
            print(f"\n--- {nome_coluna} ---")
            print(f"Média: {AnaliseEstatistica.mean(col):.2f}")
            print(f"Moda: {AnaliseEstatistica.mode(col)}")
            print(f"Mediana: {AnaliseEstatistica.median(col):.2f}")
            print(f"Desvio Padrão: {AnaliseEstatistica.std(col):.2f}")
            print(f"Variância: {AnaliseEstatistica.variance(col):.2f}")
            print(f"Intervalo: {AnaliseEstatistica.interval(col):.2f}")

            z_vals, z_outs = DeteccaoOutliers.zscore(col)
            (_, _), tukey_outs = DeteccaoOutliers.cerca_tukey(col)

            print(f"Outliers (Z-Score): {len(z_outs)} → {[ids[i] for i in z_outs]}")
            print(f"Outliers (Tukey): {len(tukey_outs)} → {[ids[i] for i in tukey_outs]}")