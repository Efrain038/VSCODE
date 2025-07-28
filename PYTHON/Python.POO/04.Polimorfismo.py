class gato:
    def sonido(self):
        return "miau"
    
class perro:
    def sonido(self):
        return "guau"
    
def hacer_sonido(animal):
    print(animal.sonido())  



Gato = gato()
Perro = perro()

hacer_sonido(Gato)

print(Perro.sonido())




























































































