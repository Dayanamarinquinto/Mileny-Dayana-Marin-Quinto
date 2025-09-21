# Definición de la función
def CalcularDescuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado sobre un monto total de compra.

    Parámetros:
    monto_total (float): Monto total de la compra.
    porcentaje_descuento (float, opcional): Porcentaje de descuento a aplicar. Por defecto es 10%.

    Retorna:
    float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Solicitar al usuario el monto de la compra
monto_usuario = float(input("Ingrese el monto total de la compra: $"))

# Llamada 1: usando el descuento por defecto (10%)
descuento_defecto = CalcularDescuento(monto_usuario)
print(f"\nUsando el descuento por defecto (10%):")
print(f"Monto total: ${monto_usuario}, Descuento aplicado: ${descuento_defecto}")

# Preguntar si desea aplicar un porcentaje de descuento diferente
respuesta = input("\n¿Desea ingresar un porcentaje de descuento diferente? (si/no): ").strip().lower()
if respuesta == "si":
    porcentaje_usuario = float(input("Ingrese el porcentaje de descuento: "))
    descuento_personalizado = CalcularDescuento(monto_usuario, porcentaje_usuario)
    print(f"\nUsando el descuento personalizado ({porcentaje_usuario}%):")
    print(f"Monto total: ${monto_usuario}, Descuento aplicado: ${descuento_personalizado}")