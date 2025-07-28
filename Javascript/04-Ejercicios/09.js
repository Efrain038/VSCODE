/**
 * crear algoritmo que devuelva un
 * array de objetos en base a pares
 */

let pairs = [
    [1, { name: "Felipe" }],
    [2, { name: "nicolas" }],
    [3, { name: "Cancho" }]
]
let array = [{
    id: 1,
    name: "felipe"
}, {
    id: 2,
    name: "nicolas"
}, {
    id: 3,
    name: "Cancho"
}]

function toCollection(arr) {
    let collection = []
    for (idx in arr) {
        let elemento = arr[idx]
        collection[idx] = elemento[1]
        collection[idx].id = elemento[0]
    }
    return collection
}

let resultado = toCollection(pairs)
console.log(resultado);
