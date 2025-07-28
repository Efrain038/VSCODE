class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

# el get es para odtener algun atributo de la clase que este en privado o muy privado ( _ ) o ( __ )

    def get_nombre(self):
        return self.__nombre
    
# el set se utiliza para cambiar el o los atributo priva.. o muy priva... de una clase, para poder cambiarlos debes obenerlos con un get antes

    def set_nombre(self,new_name):
        self.__nombre = new_name



pedro = persona("pedro",20)

nombre = pedro.get_nombre()
print(nombre)

pedro.set_nombre("maria")

nombre = pedro.get_nombre()
print(nombre)










