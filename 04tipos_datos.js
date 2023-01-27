var suma = 2 + 2;
console.log(suma);
// Tipos de javascript
var numero = 2;
var string = "soy un texto";
var booleano = false;
var array = ["aa", "bb", 3, [1, 2]];
var objeto = {
    nombre: "Lucho",
    apellido: "Bravo",
    edad: 27
};

console.log(objeto.nombre)

console.log(array[0])

var funcion = function () {
    console.log("Hola mucho gusto")
};

// Los tipos son dinamicos

var a = 8;
a = "Hola";
console.log(typeof a == "string")

// null y undefined

var valorNulo = null;
var valorUndefined = undefined;
console.log(valorNulo == valorUndefined) // Son iguales
console.log(valorNulo === valorUndefined) // Sus tipos no son iguales
console.log(typeof valorNulo, typeof valorUndefined)
