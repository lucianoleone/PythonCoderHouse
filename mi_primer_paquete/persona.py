class Persona:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return f"Nombre: {self.nombre} , Apellido: {self.apellido}"
    def agregar_persona():
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        return Persona(nombre, apellido)