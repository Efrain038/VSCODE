print("--------------------------------------------------------------------------------------")
class Celulares:
    def __init__ (self,marca,modelo,camara):
       self.marca = marca
       self.modelo = modelo
       self.camara = camara

    def llamar(self):
        print(f"estas llamamdo desde un : {self.modelo}")
    def cortar(self):    
       print(f'cortaste la llamada desde tu :{self.modelo}')



Celularar1 = Celulares("Samsung","s23","48MP")
Celularar2 = Celulares("Apple","Iphone Pro", "96MP")


Celularar1.llamar()





