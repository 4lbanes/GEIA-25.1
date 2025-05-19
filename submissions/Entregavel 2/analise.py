import numpy as np

class AnaliseEstatistica():
    def __init__(self):
        pass

    def mean(array):
        mean = np.mean(array)
        return mean 
    def mode(array):
        pass
    def median(array):
        median = np.median(array)
        return median
    def std(array):
        std = np.std(array)
        return std 
    def interval(array):
        return np.max(array) - np.min(array)
    def variance(array):
        variance = np.var(array)
        return variance
    def zscore(array):
        return (array - np.mean(array)) / np.std(array)
    def cerca_tukey(array):
        q1 = np.percentile(array, 25)
        q3 = np.percentile(array, 75)
        iqr = q3 - q1
        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr
        return limite_inferior, limite_superior
    def generate_report():
        pass