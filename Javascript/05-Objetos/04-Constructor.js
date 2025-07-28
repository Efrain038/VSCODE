// { id: 1, recuperarclave: funcion() {} }
function Usuario() {
    this.id = 1
    this.recuperando_clave = function() {
        console.log("Recuperando clave....")
    }
}

let usuario = new Usuario()
console.log(usuario)