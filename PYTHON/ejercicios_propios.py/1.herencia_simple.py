class banco:
    def __init__(self,Dinero):

        self.Dinero = Dinero
        
        
Dinero = banco(10000)

class persona(banco):
    def __init__(self,Dinero,Saldo,trabajo,pasa_tiempo):
        super().__init__(Dinero)
        self.saldo = Saldo
        self.pasa_tiempo = pasa_tiempo
        self.trabajo = trabajo
        


Dani = persona(2000,150,"programador","futbol")


print(Dani.Dinero)
























































































