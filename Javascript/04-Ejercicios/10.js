/**
 * crear array de longitud N, y que sus elementos sean
 * numeros 1 hasta N
 */

let longitud = 7

function CrearArray(n) {
    if (n <= 0) {
        return []
    }
    let arr = []
    for (let X = 0; X < n; ++X) {
        arr[X] = X + 1
    }
    return arr
}

let resultado = CrearArray(longitud)
console.log(resultado)