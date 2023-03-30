from reto3 import Persona

class Inicio2:
    def __init__(self):
        self.persona = Persona()

    def ejecutar(self):
        self.persona.pedirDatos()
        self.persona.mostrarPersona()
        self.persona.calcularImc()
        self.persona.mayorEdad()

inicio = Inicio2()
inicio.ejecutar()