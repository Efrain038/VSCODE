/**
 * crear algoritmo que tome un array de
 * objetos y devuelva un array de pares
 */

let array = [{
    id: 1,
    name: "Dani"
}, {
    id: 2,
    name: "anyi"
}, {
    id: 3,
    name: "Tony"
}]

let pares = [
    [1, { id: 1, name: "" }],
    [2, { id: 2, name: "" }],
    [3, { id: 3, name: "" }],
]

function topairs(arr) {
    let pairs = []
    for (idx in arr) {
        let elemento = arr[idx]
        pairs[idx] = [elemento.id, elemento]
    }
    return pairs
}

let resultado = topairs(array)
console.log(resultado)