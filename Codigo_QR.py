import qrcode

def generar_QR(text):
    QR = qrcode.make(text)
    QR.save("Codigo_QR.png")

text = input("CODE HTTPS:// : ")
generar_QR(text)