# Crear el diccionario inicial con información ficticia
informacion_personal = {
    "Nombres": "Dayana",   # Clave "Nombres" con valor "Dayana"
    "Edad": 19,            # Clave "Edad" con valor 19
    "Ciudad": "Sábitre"    # Clave "Ciudad" con valor "Sábitre"
}

print("Diccionario inicial:")
print(informacion_personal)
print("-" * 40)

# Acceder y modificar el valor de la clave "Nombres"
print("Valor actual de 'Nombres':", informacion_personal["Nombres"])
informacion_personal["Nombres"] = "Dayana María"
print("Después de modificar 'Nombres':", informacion_personal)
print("-" * 40)

# Acceder y modificar la clave "Ciudad"
print("Ciudad actual:", informacion_personal["Ciudad"])
informacion_personal["Ciudad"] = "Quito"
print("Después de modificar 'Ciudad':", informacion_personal)
print("-" * 40)

# Agregar nueva clave "Profesión"
informacion_personal["Profesión"] = "Ingeniera de Sistemas"
print("Después de agregar 'Profesión':", informacion_personal)
print("-" * 40)

# Verificar si existe la clave "Telefono", si no, agregarla
if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"] = "+593-9-1234-5678"
    print("La clave 'Telefono' no existía. Se agregó con un valor ficticio.")
print(informacion_personal)
print("-" * 40)

# Eliminar la clave "Edad"
if "Edad" in informacion_personal:
    del informacion_personal["Edad"]
    print("La clave 'Edad' ha sido eliminada.")
print("-" * 40)

# Imprimir el diccionario final
print("Diccionario final resultante:")
print(informacion_personal)