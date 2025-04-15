def range_(values):
    """
    Calcula o intervalo (amplitude total) dos dados.

    O intervalo é a diferença entre o maior e o menor valor da lista.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Diferença entre o valor máximo e o mínimo.
    """
    max_value = values[0]
    min_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return max_value - min_value


def mean(values):
    """
    Calcula a média aritmética de uma lista de valores numéricos.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Média aritmética.
    """
    total = 0
    count = 0
    for value in values:
        total += value
        count += 1
    return total / count


def population_standard_deviation(values):
    """
    Calcula o desvio padrão populacional.

    Mede o quanto os valores se afastam da média da população.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Desvio padrão populacional.
    """
    m = mean(values)
    total = 0
    for x in values:
        total += (x - m) ** 2
    variance = total / len(values)
    return variance ** 0.5


def sample_standard_deviation(values):
    """
    Calcula o desvio padrão amostral.

    Utilizado quando os dados representam uma amostra e não a população completa.
    Usa n - 1 no denominador (correção de Bessel).

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Desvio padrão amostral.
    """
    m = mean(values)
    total = 0
    for x in values:
        total += (x - m) ** 2
    variance = total / (len(values) - 1)
    return variance ** 0.5


def population_variance(values):
    """
    Calcula a variância populacional dos dados.

    A variância é o quadrado do desvio padrão e mede a dispersão dos dados em relação à média.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Variância populacional.
    """
    m = mean(values)
    total = 0
    for x in values:
        total += (x - m) ** 2
    return total / len(values)


def sample_variance(values):
    """
    Calcula a variância amostral.

    Utiliza n - 1 no denominador, apropriada para quando os dados são uma amostra da população.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Variância amostral.
    """
    m = mean(values)
    total = 0
    for x in values:
        total += (x - m) ** 2
    return total / (len(values) - 1)


def interquartile_range(values):
    """
    Calcula a amplitude interquartil (IQR) dos dados.

    IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1),
    representando a dispersão dos dados centrais.

    Args:
        values (list of float or int): Lista de números.

    Returns:
        float: Amplitude interquartil.
    """
    def median_calc(lst):
        m = len(lst)
        if m % 2 == 0:
            return (lst[m // 2 - 1] + lst[m // 2]) / 2
        else:
            return lst[m // 2]

    # Ordenando os valores manualmente (sem importação)
    def merge_sort(values):
        if len(values) <= 1:
            return values
        middle = len(values) // 2
        left = merge_sort(values[:middle])
        right = merge_sort(values[middle:])
        return merge(left, right)
    
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

    sorted_values = merge_sort(values)
    n = len(sorted_values)
    Q1 = median_calc(sorted_values[:n // 2])
    Q3 = median_calc(sorted_values[(n + 1) // 2:])
    return Q3 - Q1
