baul = [] 

while True:
    print("\n¿Qué deseas hacer?")
    print("1. Agregar un artículo al baúl")
    print("2. Listar artículos del baúl")
    print("3. Borrar el último artículo de la lista")
    print("4. Borrar un artículo del baúl")
    print("5. Salir")

    opcion = int(input("\nPor favor ingresa la opcion que deseas: "))

    if opcion == 1:
        articulo = input("\nIngrese el nombre del artículo a agregar: ")
        baul.append(articulo)
        print("\nEl artículo", articulo, "ha sido agregado al baúl.")

    elif opcion == 2:
        if len(baul) == 0:
            print("\nEl baúl está vacío.")
        else:
            print("\nArtículos en el baúl:")
            for i in range(len(baul)):
                print(i+1, ".", baul[i])

    elif opcion == 3:
        if len(baul) == 0:
            print("\nEl baúl ya está vacío.")
        else:
            ultimo_articulo = baul.pop()
            print("\nEl artículo", ultimo_articulo, "ha sido eliminado del baúl.")

    elif opcion == 4:
        if len(baul) == 0:
            print("\nEl baúl está vacío.")
        else:
            print("\nArtículos en el baúl:")
            for i in range(len(baul)):
                print(i+1, ".", baul[i])
            indice = int(input("\nIngrese el número del artículo a borrar: "))
            if indice > 0 and indice <= len(baul):
                articulo_borrado = baul.pop(indice-1)
                print("\nEl artículo", articulo_borrado, "ha sido eliminado del baúl.")
            else:
                print("\nEl número de artículo ingresado es inválido.")

    elif opcion == 5:
        print("Gracias por utilizar el baúl.")
        break

    else:
        print("La opción ingresada no es valida. Por favor, intente nuevamente.")