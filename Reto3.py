from random import randint

dado1=randint(1,6)
dado2=randint(1,6)

print("Resultado dados 1 y 2: ", dado1,dado2)

if dado1 == 1 and dado2 == 1:
    print("Par y Suma 2 en los datos, asi que... Ganaste!")
if dado1 == 1 and dado2 == 2:
    print("Un total de tres en los datos... asi que Ganaste")
if dado2 == 1 and dado1 == 2:
    print("Un total de tres en los datos... asi que Ganaste")
if dado1 == 6 and dado2 == 5:
    print("Da 11, asi que Ganaste")
if dado2 == 6 and dado1 == 5:
    print("Da 11, asi que Ganaste")
if dado1 == 6 and dado2 == 6:
    print("Da 12, Ganaste")
if dado1 == 5 and dado2 == 2 or dado2 == 5 and dado1 == 2 or dado1 == 3 and dado2 == 4 or dado1 == 4 and dado2 == 3 or dado1 == 6 and dado2 == 1 or dado2 == 6 and dado1 == 1:
    print("Un total de 7 en los datos, Ganaste!")
else:
    print("No cumple ningun requisito: PERDISTE! ")