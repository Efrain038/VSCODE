let Array = [
    2, 5, 8, -20, 15, 265, -258
]

function getMenorMayor(Arr) {
    let menor = Arr[0]
    let mayor = Arr[0]
    for (numero of Arr) {
        menor = menor < numero ? menor : numero
        mayor = mayor > numero ? mayor : numero
    }
    return [menor , mayor]
}

let numeros = getMenorMayor(Array)
console.log(numeros)