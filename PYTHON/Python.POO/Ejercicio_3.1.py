class animal:
    def comer(self):
        print("El animal esta comiendo")



class ave(animal):
    def volar(self):
        print("El animal esta volando")
        


class mamifero(animal):
    def amamantar(self):
        print("El animal esta amamantando")
        


class murcielago(ave,mamifero):
 pass
        

Murcielago = murcielago()

Murcielago.comer()
Murcielago.volar()
Murcielago.amamantar()




