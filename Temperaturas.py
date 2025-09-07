# Definimos parámetros
num_ciudades = 2       # cantidad de ciudades
num_semanas = 2        # semanas
dias_por_semana = 7    # días de la semana

# Creamos matriz 3D de temperaturas con datos de ejemplo
# Estructura: ciudades -> semanas -> días
temperaturas = [
    [   # Ciudad 0
        [20, 22, 21, 19, 23, 24, 25],   # Semana 0
        [18, 20, 19, 21, 22, 23, 24]    # Semana 1
    ],
    [   # Ciudad 1
        [25, 26, 27, 24, 28, 29, 30],   # Semana 0
        [22, 23, 24, 25, 26, 27, 28]    # Semana 1
    ]
]

# Calcular y mostrar el promedio para cada ciudad y semana
for ciudad in range(num_ciudades):
    print(f"\nCiudad {ciudad + 1}:")
    for semana in range(num_semanas):
        suma = 0
        for dia in range(dias_por_semana):
            suma += temperaturas[ciudad][semana][dia]
        promedio = suma / dias_por_semana
        print(f"  Semana {semana + 1}: promedio = {promedio:.2f}°C")