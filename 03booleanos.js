var booleanoCierto = true;
var booleanoFalso = false;

var a = "10";
var b = 10;

var comprobacion = a < b;

console.log(comprobacion)
// === evalua tipo de datos, !== lo mismo
console.log(a === b);

var rangoInicio = 0;
var rangoFin = 100;
var comparacion = 102;

var mayorInicio = comparacion > rangoInicio;
var menorFin = comparacion < rangoFin;

// and = &&, or = ||
var dentroDeRango = mayorInicio && menorFin;
console.log(dentroDeRango)

var hechoTrabajo = false;
var notaExaminFinal = 7;
var tieneFaltaTecnica = false;
var aprobadoCurso = (hechoTrabajo || notaExaminFinal >= 7) && !tieneFaltaTecnica;

console.log("Aprobado curso? ", aprobadoCurso)

var infUno = 5;
var supUno = 20;
var infDos = 10;
var supDos = 25;
var checkInf2Sup1 = infDos < supUno && infDos > infUno;
var checkInf1Sup2 = supDos > infUno && supDos < supUno;
var checkSuperp = checkInf1Sup2 || checkInf2Sup1;

console.log("esta superpuesto? ", checkSuperp)
