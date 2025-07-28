// personaje de TV
let nombre = "Tanjiro";
let anime = "Demon slayer";
let edad = 16;

let personaje = {
  nombre: "Tanjiro",
  anime: "Demon Slayer",
  edad: 16,
};
console.log(personaje);
console.log(personaje.edad);
console.log(personaje["nombre"]);

personaje.edad = 20;

let llave = "edad";
personaje[llave] = 11;

delete personaje.anime;
console.log(personaje);
