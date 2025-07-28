let array = [10, 23, 52, -100, -56, 156]

function CuantosPositivos(arr) {
    let Cantidad = 0
    for (elemento of arr) {
        if (elemento > 0) {
            Cantidad++
        }
    }
    return Cantidad
}

let resultado = CuantosPositivos(array)
console.log(resultado)