print("----------------------------------------------------------------------------------------------------------------")
tabla = int(input("Ingrese el numero de la tabla de multiplicar que desea ver-----> "))

def tabla_multiplicar(tabla,limite):
    for x in range (1,limite):
     resultado = tabla * x
     print(f"{tabla} x {x} = {resultado}")    

tabla_multiplicar(tabla,11)





