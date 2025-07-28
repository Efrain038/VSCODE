# 🧠 Guía definitiva de símbolos en programación (enfocada en JavaScript)

Este documento explica el uso de los principales símbolos y caracteres que ves constantemente en el código. Está pensado para ayudarte a entender lo que significan más allá de los paréntesis, con ejemplos claros y explicaciones simples.

---

## ✦⃣ 1. Paréntesis `( )`

### 📊 Uso principal:

- Agrupar operaciones matemáticas.
- Encerrar los parámetros de una función.
- Envolver condiciones en estructuras como `if`, `while`, etc.

### ✅ Ejemplo:

```js
function saludar(nombre) {
  console.log("Hola " + nombre);
}

let resultado = (2 + 3) * 4; // los paréntesis cambian el orden
```

---

## 🟢 2. Llaves `{ }`

### 📊 Uso principal:

- Delimitar bloques de código.
- Definir el cuerpo de funciones, bucles, condicionales.
- Crear objetos en JavaScript.

### ✅ Ejemplo:

```js
if (edad > 18) {
  console.log("Mayor de edad");
}

let persona = {
  nombre: "Dani",
  edad: 21
};
```

---

## 🟡 3. Corchetes `[ ]`

### 📊 Uso principal:

- Definir arrays (listas).
- Acceder a elementos por índice.
- Usar variables como clave de acceso.

### ✅ Ejemplo:

```js
let frutas = ["manzana", "pera", "uva"];
console.log(frutas[1]); // "pera"
```

---

## 🟠 4. Signos menor `<` y mayor `>`

### 📊 Uso principal:

- Comparaciones: menor que, mayor que.
- Etiquetas HTML.

### ✅ Ejemplo:

```js
if (edad < 18) {
  console.log("Eres menor de edad");
}

// En HTML
<div>
  <p>Hola mundo</p>
</div>
```

---

## 🔹 5. Comillas `""`, `''` y **backticks** `` ` ``

### 📊 Uso principal:

- Declarar strings.
- Los backticks se usan para templates con variables embebidas.

### ✅ Ejemplo:

```js
let saludo = "Hola";
let nombre = 'Dani';
let completo = `Hola, ${nombre}`;
```

---

## ⚖️ 6. Operadores comunes

| Símbolo | Significado                         | Uso Ejemplo                               |               |     |   |     |
| ------- | ----------------------------------- | ----------------------------------------- | ------------- | --- | - | --- |
| `=`     | Asignación                          | `x = 5`                                   |               |     |   |     |
| `==`    | Comparación (valor)                 | `x == "5"` → true                         |               |     |   |     |
| `===`   | Comparación estricta (valor y tipo) | `x === "5"` → false                       |               |     |   |     |
| `!`     | Negación                            | `!true` → false                           |               |     |   |     |
| `!=`    | Diferente                           | `x != 3`                                  |               |     |   |     |
| `!==`   | Diferente estricto                  | `x !== "3"`                               |               |     |   |     |
| `&&`    | Y lógico (AND)                      | `a && b`                                  |               |     |   |     |
| \`      |                                     | \`                                        | O lógico (OR) | \`a |   | b\` |
| `:`     | Separador en objetos o ternarios    | `{nombre: "Dani"}` o `cond ? "sí" : "no"` |               |     |   |     |
| `;`     | Fin de instrucción                  | `let x = 5;`                              |               |     |   |     |
| `,`     | Separador de elementos              | `[1, 2, 3]`                               |               |     |   |     |

---

## ✨ Consejo final:

> Entender estos símbolos no es solo saber lo que hacen, sino saber **cuándo usarlos y por qué**. Son como la puntuación del lenguaje del código: sin ellos, todo se rompe.

---

✊ Seguilos practicando en proyectos reales. Aprendé a leer código como si fuera una novela escrita en lógica. Y si algo te confunde, volvé a esta guía como si fuera tu diccionario personal.

