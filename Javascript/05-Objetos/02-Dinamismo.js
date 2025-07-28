const user = {id:1}

user.name = "nicolay"
user.guardar = function () {
    console.log("guardando", user)
}
user.guardar()

delete user.name
delete user.guardar
console.log(user)

const X = Object.seal({ id: 4 })
X.name = "batman"
X.id = 2
console.log(X)