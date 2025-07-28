class auto():
    def __init__(self):
        self._estado = "apagado"


    def encender(self):
        self._estado = "encendido"
        print("es auto esta encendido")


    def conducir(self):
        if self._estado == "apagado":
            self.encender()
        print("conduciendo el auto")    

           
mi_auto = auto()
mi_auto.conducir()




























































































