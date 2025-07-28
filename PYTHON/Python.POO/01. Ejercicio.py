class Estudiante:
   def __init__ (self,Nombre,Edad,Grado):
      self.Nombre = Nombre
      self.Edad = Edad
      self.Grado = Grado

   def estudiar(self):
      print("Eso Hago....")


nombre = input("Digame su Nombre --->")
edad = input("Digame su Edad ---> ")
grado = input("Digame su Grado ---> ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DE ESTUDIANTE: \n \n 
      NOMBRE : {estudiante.Nombre} \n
      EDAD : {estudiante.Edad} \n
      GRADO : {estudiante.Grado} \n
    """)


while True: 
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
      estudiante.estudiar()
     




















