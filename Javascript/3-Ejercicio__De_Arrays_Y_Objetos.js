let Estudiantes = [
    { name: "maria", Password: "3001", Age: 20, ratings: 80 },
    { name: "marco", Password: "1234", Age: 18, ratings: 77 },
    { name: "felipe", Password: "741", Age: 23, ratings: 90 },
]
let access = false
while (!access) {
    let Name_Intered = prompt("name Here ↓").trim()
    let Password_Intered = prompt("Password Here ↓").trim()

    let Y = false
    for (let student of Estudiantes) {
        if (Name_Intered == student.name && Password_Intered == student.Password) {
            alert(`Welcome back, ${Name_Intered}!\nTu calificación es: ${student.ratings}`);
            access = true
            Y = true
            break
        }
    }

    if (!Y) {
        alert("your Name Or Password Is Incorrect, Try again")
    }
}
