Prueba = [

   {"nombre": "admin", "pin": "1234" , "saldo" : "10000"},

]

usuario_nombre = input("su nombre ----->")
usuario_pin = input("ponga su pin ----->")

for X in Prueba:
    if X["nombre"] == usuario_nombre and X["pin"] == usuario_pin:
        saldo = X["saldo"]
        print(saldo)
 













