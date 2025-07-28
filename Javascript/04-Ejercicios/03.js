/*
Indice Validar Que No Sea Menor A Cero Y Que El Elemento Exista
En El Array
*/

function getbyidx(arr, idx) {
    if (idx < 0 || arr.length <= idx) {
        return "Elemento No Existe"
    }
    return arr[idx]
}

let resultado = getbyidx([1, 2], 0)
console.log(resultado)
