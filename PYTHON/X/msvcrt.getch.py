import msvcrt

print("Presiona 'q' para salir...")

while True:
    tecla = msvcrt.getch().decode()  # Captura la tecla y la decodifica a string
    if tecla.lower() == 'q':  # Sale si se presiona 'q' (mayúscula o minúscula)
        break

print("Saliste del programa.")
