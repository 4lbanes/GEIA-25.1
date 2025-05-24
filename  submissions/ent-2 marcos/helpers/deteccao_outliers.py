import numpy as np

class DeteccaoOutliers:
    """
    Classe para detecção de outliers usando Z-Score e Cerca de Tukey.
    """
    def __init__(self, dados):
        """
        Inicializa com um array de dados numéricos.
        """
        self.dados = np.array(dados)

    def zscore(self, threshold=3):
        """
        Retorna os índices dos outliers usando o método do Z-Score.
        threshold: valor limite para considerar um outlier (padrão=3).
        """
        mean = np.mean(self.dados)
        std = np.std(self.dados, ddof=1)
        if std == 0:
            return []
        z_scores = np.abs((self.dados - mean) / std)
        return list(np.where(z_scores > threshold)[0])

    def cerca_tukey(self):
        """
        Retorna os índices dos outliers usando a Cerca de Tukey (IQR).
        """
        q1 = np.percentile(self.dados, 25)
        q3 = np.percentile(self.dados, 75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return list(np.where((self.dados < lower) | (self.dados > upper))[0])