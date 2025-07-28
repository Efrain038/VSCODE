class persona:
    def __init__(self,nombre):
        self.nombre = nombre


    def set_nombre(self,new_name):
      self.nombre = new_name
      

pepe = persona("pedro")
nombre = pepe.nombre
print(nombre)

pepe.set_nombre = "maria"
nombre = pepe.set_nombre
print(nombre)










