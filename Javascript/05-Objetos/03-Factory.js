function crearUsuario (name, email) {
    return {
        id:2,
        email,
        name,
        activo: false,
        recuperar_Clave: function () {
            console.log("reperando clave")
        },
    }
}

let user1 = crearUsuario("Dani","holamundo@gmail.com")
let user2 = crearUsuario("juan","mundo@gmail.com")
let user3 = crearUsuario("pepe","hola@gmail.com")

console.log(user1,user2,user3)