numero_notas = int(input("Ingresa por favor las notas por evaluar: "))

notas = []
for i in range(numero_notas):
    nota = float(input(f"Ingresa tu nota {i+1}: "))
    while nota < 0.0 or nota > 5.0:
        nota = float(input(f"Ingresa una nota entre (0.0 y 5.0) para la nota {i+1}: "))
    notas.append(nota)

promedio = sum(notas) / numero_notas

if promedio < 3.0:
    print("\nTu nota fue menor de 3, Reprobo")
    nota_final = 0.0
elif promedio >= 3.0 and promedio < 4.0:
    print("\nTu nota esta entre 3 y 4, Paso raspando")
    nota_final = 3.5
else:
    print("\nTu nota es mayor de 4, Aprobo")
    nota_final = 5.0

print(f"\nLa nota final es: {nota_final}")