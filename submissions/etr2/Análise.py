import numpy as np

array = np.genfromtxt("base.csv", delimiter=",", skip_header=1)

idade = array[:, 1]
mat = array[:, 2]
est = array[:, 3]
prog = array[:, 4]
faltas = array[:, 5]

variaveis = {
    'Idade': idade,
    'Notas de Matemática': mat,
    'Notas de Estatistica': est,
    'Notas de Programação': prog,
    'Faltas': faltas
}

shits = np.array([idade, mat, est, prog, faltas])

def mean(array):
    return np.mean(array)

def mode(array):
    valores, counts = np.unique(array, return_counts=True)
    max = np.argmax(counts)
    return valores[max]
    # falta fazer o bimodal da silva
    
def median(array):
    return np.median(array)

def std(array):
    return np.std(array)

def interval(array):
    return np.max(array) - np.min(array)

def variance(array):
    return np.var(array)

def z_score(array):
    return (array - np.mean(array)) / np.std(array)

def cerca_turkey(array):
    q1 = np.percentile(array, 25)
    q3 = np.percentile(array, 75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return limite_inferior, limite_superior

def generate_report():

    print("A média: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {mean(variavel)}")

    print("A mediana: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {median(variavel)}")
        
    print("A moda: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {mode(variavel)}")

    print("O desvio padrão: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {std(variavel):.2f}")
    
    print("A variância: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {variance(variavel):.2f}")

    print("O intervalo: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {interval(variavel):.2f}")

    print("O Z-Score: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {z_score(variavel)}")
        # acho que tem q arredondar o caba aq

    print("Cerca de Tukey: ")
    for nome, variavel in variaveis.items():
        inf, sup = cerca_turkey(variavel)
        print(f"{nome}, Inferior: {inf:.2f}, Superior: {sup:.2f}")

    #falta fazer os outliers

generate_report()