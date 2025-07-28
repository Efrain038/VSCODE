class persona():
    def __init__(self,nombre,edad):
      self.nombre = nombre
      self.edad = edad

    # def __str__(self):
    #    return f"persona(nombre={self.nombre} , edad {self.edad})"

    # def __repr__(self):
    #    return f"persona({self.nombre} , {self.edad})"

    def __add__(self,otro):
       nuevo_valor = self.edad + otro.edad
       return persona(self.nombre + otro.nombre , nuevo_valor)
 
    def __sub__(self,otro):
       restar = self.edad - otro.edad
       return persona(self.edad - otro.edad , restar)

    def __truediv__(self,otro):
       dividir = self.edad / otro.edad
       return persona(self.edad / otro.edad , dividir)

    def __mul__(self,otro):
       multiplicar = self.edad * otro.edad
       return persona(self.edad * otro.edad , multiplicar)

    




dalto = persona("tu_lokita_",20)
pedro = persona("pedro_",60)
maria = persona("maria",18)

nueva_persona = dalto / pedro + maria
print(nueva_persona.edad)



