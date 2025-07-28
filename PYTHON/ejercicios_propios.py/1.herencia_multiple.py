class persona:
    def __init__(self,nombre,apellido,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

class empleado():
    def __init__(self,salario):
        self.salario = salario
        print("Hola Mundo")

class Habilidad(persona,empleado):
    def __init__(self,habilidad):
        self.habilidad = habilidad

pedro = Habilidad("pedro","perez","RD",10000,"volar")

print(pedro.nombre)



























































































