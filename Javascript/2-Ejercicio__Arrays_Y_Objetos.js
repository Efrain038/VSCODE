// array de objetos
let auto = [
    {
        marca: "toyota",
        año: 2000,
        color: "azul",
    }
]
console.log(auto[0].marca, auto)

// objetos
let X = {
    nombre: "Dani",
    Apellido: "Montero",
    3: "programador",
}
console.log(X.nombre, X.Apellido, "→", X[3], X)

// array de arrays
let Y = [
    ["Efrain", "Dani_Montero", "17"],
    ["batman"],
    [[["tu mama"]]]
]
console.log(Y[0][0][0], Y[1][0], Y[2][0][0], Y)

// arrays de objetos con array dentro
let a = [
    { nombre: ["maria", "pedro", "juan"], edad: ["30", "20", "50"] },
    { nombre: ["tony", "Efrain", "melquisedec"], edad: ["28", "17", "10"] },
    { nombre: ["matusalen", "habrahan", "jesus"], edad: ["510", "5", "33"] },
]
console.log(a[0].nombre[0], a)