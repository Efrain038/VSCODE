class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(
                f"nombre : {self.nombre}\n",
                f"edad  : {self.edad}"
)

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(
                f"grado : {self.grado}",
                
)

estudiante = Estudiante("pepe","20","1ro")

estudiante.mostrar_datos()
estudiante.mostrar_grado()

            





















