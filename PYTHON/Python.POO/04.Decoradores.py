def decorador(funcion):
    def funcion_moificada():
        print("antes de llamar la funcion")
        funcion()
        print("despues de llamar la funcion")
    return funcion_moificada


# def saludo():
#     print("Hola Mundo")


# saludo_modificado = decorador(saludo)
# saludo_modificado()


# esto es lo mismo que lo de arriba
@decorador
def saludo():
    print("Hola mundo")

saludo()























































































