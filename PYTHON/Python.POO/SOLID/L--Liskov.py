class Ave:
    def hacer_sonido(self):
        return "Pío pío"

class AveVoladora(Ave):
    def volar(self):
        return "Estoy volando"

class AveNadadora(Ave):
    def nadar(self):
        return "Estoy nadando"

class Pinguino(AveNadadora):  # ✅ Ahora solo hereda lo que puede hacer
    pass

gaviota = AveVoladora()
pingüino = Pinguino()

print(gaviota.hacer_sonido())  # ✅ "Pío pío"
print(gaviota.volar())         # ✅ "Estoy volando"
print(pingüino.hacer_sonido()) # ✅ "Pío pío"
print(pingüino.nadar())        # ✅ "Estoy nadando"


    # caracteristicas : 1. debe mantener la logica del padre.                  
    #                   2. no debe eliminar metodos del padre.
    #                   3. no debe  necesitar datos extras o cambiar la estructura.
    #                   4. Puede usarse en lugar del padre sin que el código falle.

# liskov no es igual que el polimorfismo pero se relacionan



