var array = ["aa", "bb", 3, [1, 2], {nombre: "name", apellido: "last_name"}];
var objeto = {
    nombre: "Lucho",
    apellido: "Bravo",
    edad: 27,
    coches: ["ferrari", "chevrolet"],
    direccion: {
        calle: "Nombre de la calle",
        numero: 7
    }
};

var item0 = array[0];
var item1 = array[1];
var item4 = array[4].nombre;
console.log(item4);

nombreCoche = objeto.coches[1];
console.log(nombreCoche);

nombreCalle = objeto.direccion.calle;
console.log(nombreCalle)
var longitud = array.length;
console.log(longitud)