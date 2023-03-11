import random

ValorPrecio = int(input("Ingrese el valor del producto")) 
CantidadProducto = int(input("Ingrese la cantidad del producto"))

valor_compra = ValorPrecio * CantidadProducto

if valor_compra > 50000:
    bolita = random.choice(["roja", "azul", "amarilla", "blanca"])
    if bolita == "roja":
        descuento = 0.1
    elif bolita == "azul":
        descuento = 0.3
    elif bolita == "amarilla":
        descuento = 0.5
    else:
        descuento = 1.0
    valor_descuento = valor_compra * descuento
    valor_final = valor_compra - valor_descuento

    print(f"Felicidades, has ganado un descuento del {descuento*100:.0f}% con la bolita {bolita}!")
    print(f"El valor final a pagar es: ${valor_final:.2f}")

else: 
    print("Lo sentimos, no has ganado ningún descuento.")


valor_pago = float(input("Ingrese el valor con el que va a pagar: "))

cambio = valor_pago - valor_final
print(f"Su cambio es: ${cambio:.2f}")
  