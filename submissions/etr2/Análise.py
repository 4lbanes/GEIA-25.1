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
    pass
    
def median(array):
    return np.median(array)

def std(array):
    pass

def interval(array):
    pass

def variance(array):
    pass

def z_score(array):
    pass

def cerca_turkey(array):
    pass

def generate_report():
    print("A média: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {mean(variavel)}")
    print("A mediana: ")
    for nome, variavel in variaveis.items():
        print(f"{nome}, {median(variavel)}")

generate_report()