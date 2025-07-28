// short-circuit

// Falso
/* 

false
0
""
null
undefined
NaN

 */

let nombre = "Juanito alcachofa";
let username = nombre || "Anonimo";
console.log(username);

function fn1() {
  console.log("soy Funcion 1");
  return true
}

function fn2() {
  console.log(" y tambien soy Funcion 2 ♥");
  return true
}

function fn3() {
  console.log(" y tambien soy Funcion 3 ♥");
  return true
}

const X = fn1() && fn2() && fn3()