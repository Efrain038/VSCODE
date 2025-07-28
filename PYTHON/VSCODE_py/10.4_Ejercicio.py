import os
os.system("cls")

 
def Calcular_precio_total (cantidad, precio_unitario):
    print("-------------------------------------------------------------------------------------------------------------------")
    precio_total = cantidad * precio_unitario
    return precio_total


def main():
    Nombre_producto = input("Ingrese el nombre del producto---------> ")    
    cantidad = int(input("Ingrese la cantidad de productos que desea comprar-------> "))
    Precio_unitario = float(input("Ingrese el precio unitario del producto-------> "))

    if cantidad <=0 or Precio_unitario <=0 :
       print("________________________________________________________________________________________________________________")
       print("la cantidad y el precio unitario deben ser mayores a 0")
       print("----------------------------------------------------------------------------------------------------------------")
    else:
       precio_total = Calcular_precio_total(cantidad, Precio_unitario)
       impuesto = precio_total * 0.15
       precio_total_con_impuesto = precio_total + impuesto
       

       print ("----------------------------------------------------------------------------------------------------------------") 
       print ("Resumen de la compra")
       print (f"Producto: {Nombre_producto}")
       print (f"Cantidad: {cantidad}")
       print (f"Precio unitario: {Precio_unitario:.2f} ·$")
       print (f"Precio total: {precio_total:.2f} ·$")
       print (f"impuesto: {impuesto:.2f} ·$")
       print ("____________________________________________________________")
       print (f"Precio total con impuesto: {precio_total_con_impuesto}")
       

main()




