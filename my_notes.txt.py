# Tarea: Trabajo con Archivos de Texto en Python

# 1. Escritura de Archivo de Texto
with open("my_notes.txt", "w") as archivo:  # crea el archivo en modo escritura
    archivo.write("Mi nombre es Dayana.\n")
    archivo.write("Tengo 19 años.\n")
    archivo.write("Vivo en Sábitre.\n")
    archivo.write("Estoy aprendiendo Python.\n")
    archivo.write("Mi objetivo es mejorar mis habilidades en programación.\n")

# 2. Lectura de Archivo de Texto
with open("my_notes.txt", "r") as archivo:  # abre el archivo en modo lectura
    lineas = archivo.readlines()  # lee todas las líneas en una lista

# Mostrar el contenido línea por línea
for linea in lineas:
    print(linea.strip())  # strip() elimina saltos de línea adicionales

# 3. Cierre de Archivos
# Nota: al usar 'with open(...) as archivo', el archivo se cierra automáticamente.