import os
os.system("cls")

print("El valor de __name__ es:", __name__)

def saludar():
    print("¡Hola desde el módulo!")

if __name__ == '__main__':
    print("Este archivo se está ejecutando directamente")
