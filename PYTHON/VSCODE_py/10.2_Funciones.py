empresas = [6561001,23,77,44,51,24,55,545,484,65146,51616,1110,51,65165,6516,616,165,151,5,61,5,61564,25,68,469,1984984,69665,8997,1122,]

def facturacion_media(empresas):
    total = sum(empresas)
    media = total /len(empresas)
    return media


resultado = facturacion_media(empresas)   

print(f"La facturacion media de las empresas es: {resultado:.2f}")




