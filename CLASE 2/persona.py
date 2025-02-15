class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad
    
    def saludar(self):
        año = 2025
        return f' Hola, mi nombre es {self.nombre}, y es el año {año}'
    
    def despedirse(self):
        return f'adios'
    
