import qrcode

data = "Enlaces (Avanzado)/index.html"
qr = qrcode.make(data)
qr.save("codigo QR.png")