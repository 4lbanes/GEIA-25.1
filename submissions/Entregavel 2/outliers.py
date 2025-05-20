import numpy as np

class DeteccaoOutliers():
    @staticmethod
    def zscore(array):
        score = (array - np.mean(array)) / np.std(array)
        return score, np.where(abs(score) > 3)[0]
    @staticmethod
    def cerca_tukey(array):
        q1 = np.percentile(array, 25)
        q3 = np.percentile(array, 75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        indice = np.where((array < limite_inferior) | (array > limite_superior))[0]
        return (limite_inferior, limite_superior), indice