print("-----------------------------------------------------------------------------------------------------------------------------")
 
import random

print("Bienvenido al juego")
print("adivina el numero")

numero_secreto = (random.randint(1,100))

adivinado = False

while not adivinado:
    numero_usuario = int(input("Introduce un numero: "))

    if(numero_usuario == numero_secreto):
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("Has adivinado el numero ♥")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        adivinado = True
    elif numero_usuario < numero_secreto:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("el numero es mas alto")
    else:
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("el numero es mas bajo")





