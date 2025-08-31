# Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

# Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).

# Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).

# Muestra la matriz original y la matriz con la fila ordenada.


matriz = [
    [8, 5, 7],
    [3, 9, 6],
    [2, 1, 4]
]

def mostrar_matriz(m):
    for fila in m:
        print(fila)

def ordenar_matriz(m):
    lista_plana = [num for fila in m for num in fila]
    n = len(lista_plana)
    for i in range(n-1):
        for j in range(n - i -1):
            if lista_plana[j] > lista_plana[j+1]:
                lista_plana[j], lista_plana[j+1] = lista_plana[j+1], lista_plana[j]
    return lista_plana  # Devuelve la lista ordenada

# Mostrar matriz original
print("Matriz original:")
mostrar_matriz(matriz)

# Ordenar y reconstruir la matriz
lista_plana = ordenar_matriz(matriz)
filas = len(matriz)
columnas = len(matriz[0])
nueva_matriz = []
k = 0
for i in range(filas):
    nueva_fila = []
    for j in range(columnas):
        nueva_fila.append(lista_plana[k])
        k += 1
    nueva_matriz.append(nueva_fila)

print("Matriz ordenada:")
mostrar_matriz(nueva_matriz) 