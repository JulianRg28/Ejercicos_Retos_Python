class Persona:
    def __init__(self):
        self.tipoDoc = ""
        self.documento = ""
        self.nombre = ""
        self.apellido = ""
        self.peso = 0.0
        self.estatura = 0.0
        self.edad = 0
        self.sexo = ""

    def pedirDatos(self):
        self.tipoDoc = input("Ingrese tipo de documento: ")
        self.documento = input("Ingrese numero de documento: ")
        self.nombre = input("Ingrese el nombre: ")
        self.apellido = input("Ingrese el apellido: ")
        self.peso = float(input("Ingrese el peso: "))
        self.estatura = float(input("Ingrese la estatura: "))
        self.edad = int(input("Ingrese la edad: "))
        self.sexo = input("Elija el genero (M/F): ").upper()

    def mostrarPersona(self):
        print("Tipo de documento:", self.tipoDoc, "\n"
              "Número de documento:", self.documento, "\n"
              "Nombre:", self.nombre, "\n"
              "Apellido:", self.apellido, "\n"
              "Peso:", self.peso, "\n"
              "Estatura:", self.estatura, "\n"
              "Edad:", self.edad, "\n"
              "Sexo:", self.sexo, "\n")
        
    def calcularImc(self):
        pesoActual = self.peso / (self.estatura ** 2)
        if pesoActual < 20:
            print("El peso está por debajo de lo ideal")
        elif pesoActual >= 20 and pesoActual <= 25:
            print("El peso es el ideal")
        else:
            print("Tiene sobrepeso")

    def mayorEdad(self):
        if self.edad >= 18:
            print("Mayor de edad")
        else:
            print("Menor edad")