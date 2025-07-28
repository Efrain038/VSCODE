from abc import ABC , abstractstaticmethod


class persona(ABC):
    @abstractstaticmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        


    @abstractstaticmethod
    def hacer_actividad(self):
        pass


    def presentarse(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años :D")


class estudiante(persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        

    def hacer_actividad(self):
        print(f"estoy estudiando {self.actividad}")


dani = estudiante("pedro",20,"masculino","correr")

dani.hacer_actividad



















































































