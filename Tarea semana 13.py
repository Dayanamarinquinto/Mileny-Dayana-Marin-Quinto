def promedio_temperaturas(datos):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
    datos (dict): Diccionario con ciudades como claves y listas de semanas con temperaturas como valores.

    Retorna:
    dict: Diccionario con el promedio de temperaturas por ciudad.
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        suma = 0
        conteo = 0

        for semana in semanas:
            suma += sum(semana)  # suma de las temperaturas de la semana
            conteo += len(semana)  # número de días registrados

        if conteo > 0:
            promedios[ciudad] = suma / conteo
        else:
            promedios[ciudad] = None  # si no hay datos

    return promedios


# Ejemplo de uso
datos_temperaturas = {
    "Quito": [
        [15, 16, 17, 18, 16, 15, 14],
        [14, 15, 16, 17, 15, 14, 13]
    ],
    "Guayaquil": [
        [28, 29, 30, 31, 30, 29, 28],
        [27, 28, 29, 30, 29, 28, 27]
    ]
}

print(promedio_temperaturas(datos_temperaturas))