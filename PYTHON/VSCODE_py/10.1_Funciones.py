print("----------------------------------------------------------------------------------------------------------------")
empresa1 = float(input("igrese el valor en bolsa de su enmpresa 1 de la empresa-----> "))
empresa2 = float(input("igrese el valor en bolsa de su enmpresa 2 de la empresa-----> "))
empresa3 = float(input("igrese el valor en bolsa de su enmpresa 3 de la empresa-----> "))

def valor(empresa1, empresa2, empresa3):
   suma = empresa1 + empresa2 + empresa3
   valor_en_bolsa = suma / 3
   print(f"El valor en bolsa de las empresas es: {valor_en_bolsa:.2f}")

print(valor(empresa1, empresa2, empresa3))









