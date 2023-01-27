// var contador = 0;
// var N = 50;
// while (contador < N) {
//     console.log(contador);
//     contador += 1;
// }

// Hacer la orden y luego verificar la condicion.
// do {

// } while(condicion)

for (var i = 0; i < 10; i += 2) {
    console.log(i);
}

var array = [10, 20, 30];
var estudiantes = [
    {
        nombre: "estudiante 1",
        nota: 8
    },
    {
        nombre: "estudiante 2",
        nota: 1
    },
    {
        nombre: "estudiante 3",
        nota: 6
    }
]

for (let estudiante of estudiantes) {
    console.log(estudiante.nombre, estudiante.nota);
}

var estudianteAuxiliar = {
    nombre: "Luis Bravo",
    nota: 10
}
for (let key in estudianteAuxiliar) {
    console.log(estudianteAuxiliar[key]); // Similar al punto, pero es propiedad
}

var pisos = 6;
var multEspacio = pisos;
var aster = "*";
var espacio = " ";
var multAster = 1;

for (var i = 0; i < pisos; ++i) {
    console.log(espacio.repeat(multEspacio) + aster.repeat(multAster));
    multAster += 2;
    multEspacio -= 1;
}
