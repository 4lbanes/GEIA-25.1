from src.utils.utils import sum_custom, len_custom, merge_sort, counter_custom

def mean(values):
    """
    Calcula a média aritmética de uma lista de valores numéricos.

    A média é a soma de todos os valores dividida pela quantidade total de elementos.
    
    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Média aritmética dos valores.
    """
    return sum_custom(values) / len_custom(values)


def median(values):
    """
    Calcula a mediana de uma lista de valores numéricos.

    A mediana é o valor central em uma lista ordenada.
    - Se a quantidade de elementos for ímpar, retorna o valor do meio.
    - Se for par, retorna a média dos dois valores centrais.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Valor da mediana.
    """
    ordered = merge_sort(values)
    n = len_custom(ordered)
    middle = n // 2
    if n % 2 == 0:
        return (ordered[middle - 1] + ordered[middle]) / 2
    else:
        return ordered[middle]


def mode(values):
    """
    Calcula a(s) moda(s) de uma lista de valores numéricos.

    A moda é o valor que mais se repete na lista. Pode haver:
    - Uma moda (unimodal)
    - Duas ou mais modas (multimodal)
    - Nenhuma moda se todos os valores ocorrerem com mesma frequência

    Args:
        values (list of float or int): Lista de números.

    Returns:
        list: Lista com o(s) valor(es) mais frequente(s).
    """
    counts = counter_custom(values)
    max_freq = 0
    for v in counts:
        if counts[v] > max_freq:
            max_freq = counts[v]

    modes = []
    for v in counts:
        if counts[v] == max_freq:
            modes.append(v)

    return modes
