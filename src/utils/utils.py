def sum_custom(values):
    """
    Soma todos os valores de uma lista de números.

    Args:
        values (list of int or float): Lista de números.

    Returns:
        float: Soma total dos valores.
    """
    total = 0
    for v in values:
        total += v
    return total


def len_custom(values):
    """
    Conta quantos elementos existem em uma lista.

    Args:
        values (list): Lista de elementos.

    Returns:
        int: Quantidade de elementos na lista.
    """
    count = 0
    for _ in values:
        count += 1
    return count


def merge_sort(values):
    """
    Ordena uma lista de valores numéricos utilizando o algoritmo Merge Sort.

    Args:
        values (list of int or float): Lista de números.

    Returns:
        list: Lista ordenada em ordem crescente.
    """
    if len_custom(values) <= 1:
        return values

    middle = len_custom(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])

    return merge(left, right)


def merge(left, right):
    """
    Função auxiliar que combina duas listas ordenadas em uma única lista ordenada.

    Args:
        left (list): Primeira lista ordenada.
        right (list): Segunda lista ordenada.

    Returns:
        list: Lista combinada e ordenada.
    """
    result = []
    i = 0
    j = 0
    while i < len_custom(left) and j < len_custom(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len_custom(left):
        result.append(left[i])
        i += 1
    while j < len_custom(right):
        result.append(right[j])
        j += 1
    return result


def counter_custom(values):
    """
    Conta a frequência de cada valor em uma lista.

    Args:
        values (list): Lista de elementos.

    Returns:
        dict: Dicionário com os valores como chaves e as frequências como valores.
    """
    counts = {}
    for v in values:
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1
    return counts
