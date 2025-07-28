let obj = {}
let obj2 = new Object()

/**
 * nwe Array; []
 * new String(); ""  ''  ´´
 * new Number(); 1242
 * bew Boolean(); true False
 */

function Usuario() {
    this.name = "hola Mundo"
}

let user = new Usuario()
console.log(user.constructor)

const s1 = "1 + 1"
const s2 = new String("1 + 1")
console.log(eval(s1) ,eval(s2))
console.log(s2.valueOf())