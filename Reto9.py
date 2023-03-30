numero_competidores = int(input("Ingresa por favor el número de competidores: "))

competidor = {}

for i in range(numero_competidores):
    nombre = input("Ingresa el nombre del competidor {}: ".format(i+1))
    competidor[nombre] = None

for nombre in competidor:
    tiempo = float(input("Ingrese el tiempo de {}: ".format(nombre)))
    competidor[nombre] = tiempo

print("\nTiempo registrado:")
for nombre, tiempo in competidor.items():
    print("{}: {}".format(nombre, tiempo))

ganador = min(competidor, key=competidor.get)
print("\nEl ganador es: {} con un tiempo de {} segundos".format(ganador, competidor[ganador]))