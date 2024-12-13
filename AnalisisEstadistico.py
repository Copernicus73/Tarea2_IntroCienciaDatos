def medArit(datos):

    """
    Calcula la media aritmética (promedio) de una lista de datos.

    La media aritmética se define como la suma de todos los valores 
    de una lista dividida entre la cantidad de valores en la lista.

    Parámetros:
        datos (list): Lista de números (int o float) para los que se calculará la media aritmética.

    Retorna:
        float: La media aritmética (promedio) de los valores en la lista.
    """

    # Cantidad de datos.
    n = len(datos)

    # Suma total de los datos.
    suma = sum(datos)

    # Promedio de los datos
    promedio = (suma / n)

    # Retorna el promedio de los datos
    return promedio 


def mediana(datos):
    
    """
    Calcula la mediana de una lista de datos.

    La mediana es el valor medio de un conjunto de datos ordenados. 
    Si el número de elementos es impar, la mediana es el valor en la posición central.
    Si es par, la mediana es el promedio de los dos valores centrales.

    Parámetros:
        datos (list): Lista de números (int o float).

    Retorna:
        float: La mediana del conjunto de datos.
    """
    
    # Ordenar los datos de menor a mayor.
    datos.sort()

    # Cantidad de datos
    n = len(datos)

    # Índice del valor medio menor
    valorMedio = n // 2
	
    # Si el número de elementos es impar, devolver el valor medio
    if n % 2 != 0:
        mediana = datos[valorMedio]
        return mediana
	
    # Si el número de elementos es par, devolver el promedio de los valores medios
    else:
        mediana = (datos[valorMedio] + datos[valorMedio - 1]) / 2
        return mediana


def moda(datos):
    """
    Calcula la moda de una lista de datos y retorna los resultados como una tupla de strings.
    
    Parámetros:
        datos (list): Lista de números o elementos de cualquier tipo comparable, cuyos valores se utilizarán para calcular la moda.
        
    Retorna:
        tuple | bool: 
            - Si existe moda, retorna una tupla con:
                - Una cadena que contiene el/los valores de la moda separados por comas.
                - Una cadena que contiene la frecuencia máxima asociada a la moda.
            - Si no existe moda, retorna False.
    
    Nota:
        Si no existe moda (cuando todos los valores tienen la misma frecuencia), la función retorna False.
    """
    # Diccionario para almacenar el valor y su frecuencia.
    frecuencias = {}

    for dato in datos:
        if dato in frecuencias:
            # Incrementa la frecuencia si el valor ya existe.
            frecuencias[dato] += 1
        else:
            # Si el valor no existe, lo agrega con frecuencia 1.
            frecuencias[dato] = 1
    
    # Encuentra el valor o los valores con mayor frecuencia.
    frecuenciaMax = max(frecuencias.values())
    valorModa = [valor for valor, frecuencia in frecuencias.items() if frecuencia == frecuenciaMax]
    
    # En caso de no existir moda (todos los valores tienen la misma frecuencia).
    if frecuenciaMax == 1:
        return False

    # Retorna el o los valores que más se repiten y su frecuencia.
    else:
        valorModa = ", ".join(map(str, valorModa))
        frecuenciaMax = str(frecuenciaMax)
        return (valorModa, frecuenciaMax)


def rango(datos):

    """
    Calcula el rango de una lista de datos.

    El rango se define como la diferencia entre el valor máximo y el valor mínimo de los datos.

    Parámetros:
        datos (list): Lista de números (int o float) sobre los que se calculará el rango.

    Retorna:
        float: El rango de los datos, calculado como la diferencia entre el valor máximo y el mínimo.
    """

    # Rango de los datos.
    rango = max(datos) - min(datos)

    # Retorna el rango de los datos.
    return rango


def varia(datos):

    """
    Calcula la varianza de una lista de datos.

    La varianza indica la dispersión o variabilidad de los datos respecto al promedio.
    Se calcula como la media de los cuadrados de las diferencias entre cada dato y la media aritmética de los datos.

    Parámetros:
        datos (list): Lista de números (int o float) de la cual se calculará la varianza.

    Retorna:
        float: El valor de la varianza calculada utilizando la fórmula poblacional.

    Nota:
        La fórmula utilizada aquí es la población completa (no muestral),
        por lo que la división se hace entre n en lugar de (n-1).
    """

    # Ordenar los datos de menor a mayor.
    datos.sort()

    # Cantidad de datos.
    n = len(datos)

    # Promedio de los datos.
    promedio = medArit(datos)

    # Calcula el numerador de la fórmula para cada dato.
    diferenciaCuadrada = []
    for dato in datos:
        # Luego se guardan en una lista.
        diferenciaCuadrada.append((dato - promedio) ** 2)
    
    # Varianza de los datos.
    varianza = sum(diferenciaCuadrada) / (n)
    # Retorna la varianza.
    return varianza


def STD(datos):

    """
    Calcula la desviación estándar (STD) de una lista de datos.

    La desviación estándar mide la dispersión o variabilidad de un conjunto de datos. 
    Es la raíz cuadrada de la varianza, lo que indica cuánto se desvían los datos respecto al promedio.

    Parámetros:
        datos (list): Lista de números (int o float) para los que se calculará la desviación estándar.

    Retorna:
        float: La desviación estándar (STD) de los datos, redondeada a dos decimales.
    """

    # Desviacón estándar de los datos.
    STD = varia(datos) ** 0.5
    
    # Retorna la desviación estándar.
    return STD


def perc(datos):

    """
    Calcula los percentiles de una lista de datos. 
    Los percentiles devueltos son valores en las posiciones correspondientes a cada 1%, 2%, ..., 99% de los datos.

    Parámetros:
        datos (list): Lista de números (int o float) de la que se calcularán los percentiles. 
                      La lista debe ser no vacía.

    Retorna:
        list: Lista de los percentiles ordenados de la lista de datos. La lista contiene 99 elementos,
              correspondientes a los percentiles 1% a 99%.

    Nota:
        - El cálculo del percentil se realiza tomando la posición entera truncada.
    """

    # Ordenar los datos de menor a mayor.
    datos.sort()
    
    # Cantidad de datos.
    n = len(datos)

    # Lista para los datos.
    percentiles = []
    
    # Calcular los percentiles.
    for i in range(1, 100):
        # Calcular la posición del percentil.
        percentil_index = (n * i) // 100
        
        # Obtener el valor del percentil y agregarlo a la lista
        percentiles.append(datos[percentil_index])
    
    # Retorna la lista correspondiente.
    return percentiles


def IQR(datos):

    """
    Calcula el rango intercuartílico (IQR) de una lista de datos.
    El IQR es la diferencia entre el percentil 75 (Q3) y el percentil 25 (Q1) de los datos ordenados.

    Parámetros:
        datos (list): Lista de números (int o float) para los cuales se calculará el IQR.

    Retorna:
        float: El rango intercuartílico (IQR) de los datos.
               Este valor es la diferencia entre el percentil 75 y el percentil 25 de los datos ordenados.

    Nota:
        Teniendo en cuenta que es una lista los datos se cuentan como n - 1.

    """

    # Se requieren los percentiles para calcular esto.
    percentiles = perc(datos)

    # Se calcula el rango intercuartílico.
    IQR = (percentiles[74] - percentiles[24])

    # Retorna el rango intercuartílico.
    return IQR


def MAD(datos):

    """
    Calcula la desviación absoluta media (MAD) de una lista de datos.
    La MAD mide la dispersión de los datos, calculando la media de las diferencias absolutas entre cada dato y la media aritmética.

    Parámetros:
        datos (list): Lista de números (int o float) de los cuales se calculará la MAD.

    Retorna:
        float: La desviación absoluta media (MAD) de los datos.
    """

    # Ordenar los datos de menor a mayor.
    datos.sort()

    # Cantidad de datos.
    n = len(datos)

    # Promedio de los datos.
    promedio = medArit(datos)

    # Calcula el numerador de la fórmula para cada dato.
    diferenciaAbsoluta = []
    for dato in datos:
        # Luego se guardan en una lista.
        diferenciaAbsoluta.append(abs(dato - promedio))

    MAD = sum(diferenciaAbsoluta) / n

    return MAD