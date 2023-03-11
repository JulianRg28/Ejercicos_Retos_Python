import time
from time import sleep
import random

uno = ["piedra" , "papel" ,"tijeras"]
two ="-" * 15

while True:
    user =input("Elije : piedra, papel o tijeras: ").lower()
    sleep(0.9)
    if user not in uno:
        print("\nMovimiento no valido")
        continue
    pc = random.choice(uno)
    sleep(0.9)
    print(f"\nLa compu ha seleccionado {pc}")
    sleep(0.9)
    if user == pc:
        print(f"\nEmpate, ambos eligieron {user}")
    elif user =="piedra" and pc == "tijeras":
        print(f"\nGanaste,{user} en contra de {pc}")
    elif user =="tijera" and pc == "papel":
        print(f"\nGanaste,{user} en contra de {pc}")
    elif user =="papel" and pc == "piedra":
        print(f"\nGanaste,{user} en contra de {pc}")
    else:
        print(f"\nPerdiste, {user} pierde en contra {pc}")
    sleep(0.9)
    print (f"{two}Fin del juego{two}")