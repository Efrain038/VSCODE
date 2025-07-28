const Usuarios = [
    { "Nombre": "Dani", "Pin": "1234" , "Saldo" : "2500" },
    { "Nombre": "Tony", "Pin": "0000" , "Saldo" : "15000" },
    { "Nombre": "Juan", "Pin": "3001" , "Saldo" : "7500" },
]

let acceso = false
while (!acceso) {
    let Nombre_Ingresado = prompt("Name :")
    let Pin_Ingresado = prompt("Pin :")
    
    for (let User of Usuarios) {
        if (User.Nombre == Nombre_Ingresado && User.Pin == Pin_Ingresado) {
        }
    }
    if (acceso) {
        alert("Bienvenido," +Nombre_Ingresado+"!")
        console.log("Nombre y pin correctos")
    } else {
        let salir = confirm("Datos incorrectos. ¿Querés intentarlo de nuevo?")
        if (!salir) {
            alert("Nos vemos Pronto ♥")
            window.close()
            break
        }
    }
}





