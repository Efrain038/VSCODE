class Hamburguesa:
    def __init__(self):
        self.ingredientes = ["Pan", "Carne", "Lechuga"]

    def mostrar_ingredientes(self):
        return f"Ingredientes: {" - ".join(self.ingredientes)}"

# Hamburguesa con Tocino (hereda de Hamburguesa)
class HamburguesaConTocino(Hamburguesa):
    def __init__(self):
        super().__init__()  # Llama al constructor de Hamburguesa
        self.ingredientes.append("Tocino")  # Agrega tocino

# Crear hamburguesas
hamburguesa_normal = Hamburguesa()
hamburguesa_tocino = HamburguesaConTocino()

print(hamburguesa_normal.mostrar_ingredientes())  # Ingredientes: Pan, Carne, Lechuga
print(hamburguesa_tocino.mostrar_ingredientes())  # Ingredientes: Pan, Carne, Lechuga, Tocino











