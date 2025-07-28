/**
 * crear algoritmo que devuelva
 * el precio del producto
 * mas impustos
 */

function Precio_Completo(precio, impuestos) {
    return precio + precio * impuestos
}

let resultado = Precio_Completo(19.90, 0.15)
console.log(resultado)