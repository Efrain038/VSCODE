let user = {
    id: 1,
    name: "Dani",
    age: 20,
}

for (let prop in user) {
    console.log(prop, user[prop])
}
3
let animales = ["cerdo", "conejo", "hormiga"]
for (let indice in animales) {
    console.log(indice, animales[indice])
}