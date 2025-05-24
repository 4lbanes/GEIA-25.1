import numpy as np
from collections import Counter  # Import necessário para mode

class AnaliseEstatistica:
    """
    Classe para realizar análise estatística descritiva em um conjunto de dados numéricos.
    """
    def __init__(self, dados):
        # Converte os dados para array numpy para facilitar os cálculos
        self.dados = np.array(dados)

    def media(self):
        """Retorna a média dos dados."""
        return np.mean(self.dados)

    def mode(self):
        """Retorna a moda dos dados."""
        c = Counter(self.dados)
        return c.most_common(1)[0][0]

    def median(self):
        """Retorna a mediana dos dados."""
        return np.median(self.dados)

    def std(self):
        """Retorna o desvio padrão amostral dos dados."""
        return np.std(self.dados, ddof=1)

    def variance(self):
        """Retorna a variância amostral dos dados."""
        return np.var(self.dados, ddof=1)

    def interval(self):
        """Retorna o menor e o maior valor dos dados."""
        return (float(np.min(self.dados)), float(np.max(self.dados)))