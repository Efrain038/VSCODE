class Personas:
    def __init__(self,Nombre,Edad,Nacionalidad):
        self.Nombre = Nombre
        self.edad = Edad
        self.Nacionalidad = Nacionalidad
    
    def Hablar(self):
         print("Estoy Hablando")


class artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"mi habilidad es ---> {self.habilidad}")



class empleador_artista(Personas,artista):
    def __init__(self,Nombre,Edad,Nacionalidad,habilidad,empresa,salario):
        Personas.__init__(self,Nombre,Edad,Nacionalidad)
        artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        print(f"hola soy {self.Nombre} soy de {self.Nacionalidad} mi habilidad es {self.habilidad} y soy {self.empresa}")
        

roberto = empleador_artista("roberto",50,"Peru","cantar","programador",10000)

herencia = issubclass(empleador_artista,Personas)
print(herencia)


























