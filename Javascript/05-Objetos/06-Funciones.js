function Usuario(nombre) {
    this.nombre = nombre
}

console.log(Usuario.name)
console.log(Usuario.length)

const U = Usuario
let user = new U("Victor Resnon")
console.log(user)