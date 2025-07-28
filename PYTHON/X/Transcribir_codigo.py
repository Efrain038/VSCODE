# Limpiamos Todo
import os
os.system("cls")
print("_____________________________________________________")
# Lista de usuarios y contraseñas
usuario = [
    {"Nombre": "admin" , "Contraseña": "admin" , "saldo" : "15000"},
    {"Nombre": "pedro" , "Contraseña": "abc"},
    {"Nombre": "maria" , "Contraseña": "321"}
]

print("necesitare sus Datos")
print()
NombreIngresado = input("Introduzca su nombre ---> ")
ContraseñaIngresada = input("Introduzca su Contraseña ---> ")

encontrada = False

#  Vemos Si Los Datos Ingresados son Verdaderos
for X in usuario: 
    if X["Nombre"] == NombreIngresado and X["Contraseña"] == ContraseñaIngresada:
          encontrada = True
          saldo = int(X["saldo"])
          break
    

# codigo
if encontrada == True:
    
  bucle_2 = False
  while bucle_2 == False:

    import os
    os.system("cls")

    OpcionUsuario = int(input(""
                              
    "bienvenido ♥ \n"
    "______________________________________________ \n"                          
    "Menu Principal \n"
    "           1. Ver Saldo Neto $ \n"
    "           2. Depositar \n"
    "           3. Retirar \n"
    "           4. Salir \n"                               
""))     

    match OpcionUsuario:
          case 1:
            import os
            os.system("cls")
            print("-----------------")
            print(saldo)
            import msvcrt
            tecla = msvcrt.getch()

          case 2:
          
            print("-------------------------------------")
            ingresar = int(input("Que Cantidad Quiere Ingresar ------> "))
            print("-------------------------------------")
            saldo = saldo + ingresar
            print("Ingreso en Dinero Correctamente,\ngracias Por Usar Nuestros Servicios $♥$")
            import msvcrt
            tecla = msvcrt.getch()



          case 3: 
            print("-------------------------------------")
            Retirar = int(input("Que Cantidad Quiere Retirar ---->"))
            print("-------------------------------------")
            if saldo < Retirar:
              print("saldo insuficiente")
            elif saldo > Retirar:
              saldo = saldo - Retirar
              print("La cantidad Fue Retirada con Exito,\n!Gracias Por Su Confianza! ♥")
              import msvcrt
              tecla = msvcrt.getch()

          case 4:
            print("Gracias Por su tiempo ♥")
            bucle_2 = True
            import msvcrt
            tecla = msvcrt.getch()

    if OpcionUsuario >= 5:
      print("Opcion No Disponible")
      import msvcrt
      tecla = msvcrt.getch()

else:
  import os
  os.system("cls")
  print("-------------------------------------")
  print("Intenlo De Nuevo")














































