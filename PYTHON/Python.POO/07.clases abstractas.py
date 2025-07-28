import os
os.system ("cls")

from abc import ABC, abstractclassmethod

class persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad


    @abstractclassmethod
    def hacer_actividad(self):
        pass       


    def presentarse(self):
        print(f"Hola,me llamo: {self.nombre} y tengo {self.edad} años")


class Estudiante(persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")


class Trabajador(persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

    def hacer_actividad(self):
        print(f"estoy trabajando de: {self.actividad}")

pepito = Estudiante("pepito",12,"maricon","programacion")
dalto = Trabajador("dalto",30,"masculino","programador")


dalto.presentarse()
dalto.hacer_actividad()
print()
pepito.presentarse()
pepito.hacer_actividad()




































































