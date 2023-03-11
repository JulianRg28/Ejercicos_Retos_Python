from random import randint
a=randint(1,4)

compra = int(input("Ingresar compra total del cliente: "))

if compra >= 50000:
  if a==1:
   print("Felicidades, sacaste bolita roja. Tienes un descuento del 10%")
   compra = (compra / 100) * 10
   print()
   print("Tu descuento es de: ", compra)
    
  if a==2:
    print("Felicidades, sacaste bolita AZUL. Tienes un descuento del 30%")
    compra = (compra / 100) * 30
    print()
    print("Tu descuento es de: ", compra)
    
  if a==3:
    print("Felicidades, sacaste bolita AMARILLA. Tienes un descuento del 50%")
    compra = (compra / 100) * 50
    print()
    print("Tu descuento es de: ", compra)
    
  if a==4:
    print("Felicidades, sacaste bolita BLANCA. Te llevas la compra gratis!")
    compra = compra - compra
    print()
    print("Tiene que pagar: ", compra)

else:
  print()
  print("¡Gracias por comprar con nosotros!")