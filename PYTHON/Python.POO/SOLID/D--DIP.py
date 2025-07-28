class MetodoNotificacion:
    def enviar_mensaje(self, mensaje):
        pass  # No define cómo, solo qué hace

class WhatsApp(MetodoNotificacion):
    def enviar_mensaje(self, mensaje):
        print(f"📲 WhatsApp: {mensaje}")

class Email(MetodoNotificacion):
    def enviar_mensaje(self, mensaje):
        print(f"📧 Email: {mensaje}")

class Notificacion:
    def __init__(self, metodo: MetodoNotificacion):
        self.metodo = metodo

    def notificar(self, mensaje):
        self.metodo.enviar_mensaje(mensaje)

# Ahora podemos cambiar el método sin tocar Notificacion
noti1 = Notificacion(WhatsApp())
noti2 = Notificacion(Email())

noti1.notificar("Hola!")  # 📲 WhatsApp: Hola!
noti2.notificar("Hola!")  # 📧 Email: Hola!



