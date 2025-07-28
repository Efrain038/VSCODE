class Personas:
    def __init__(self,Nombre,Edad,Nacionalidad):
        self.Nombre = Nombre
        self.edad = Edad
        self.Nacionalidad = Nacionalidad
    
    def Hablar(self):
         print("Estoy Hablando")


class Empleados(Personas):
    def __init__(self,Nombre,Edad,Nacionalidad,trabajo,salario):
        super().__init__(Nombre,Edad,Nacionalidad)
        self.trabajdo = trabajo
        self.salario = salario





roberto = Empleados("roberto",50,"Peru","programador",10000)

print(roberto.trabajdo)

roberto.Hablar()




























