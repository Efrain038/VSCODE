class persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter   
    def nombre(self,new_name):
        self.__nombre = new_name


    @nombre.deleter
    def nombre(self):
        del self.__nombre




pedro = persona("pedro",20)

nombre = pedro.nombre
print(nombre)

pedro.nombre = "pepito"

nombre = pedro.nombre
print(nombre)
 

del pedro.nombre























































































