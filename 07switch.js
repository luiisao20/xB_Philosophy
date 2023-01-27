var estado = 0;

if (estado === 0) {
    // Hago A 
} else if (estado === 1) {

}

switch (estado){
    case 0: // En el caso donde estado sea 0 definimos bloque, no se puede hacer comprobaciones booleanas
        break; // Es necesario el break porque sino sigue ejecutando el resto
    case 1:
        break;
    case 2:
        break;
    default:
        break;
}
var month31 = ["Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"];
var month28 = ["Febrero"];
var month30 = ["Abril", "Junio", "Septiembre", "Noviembre"];
var monthUnknown = "Noviembre";
var estado = null;

if (month31.includes(monthUnknown)) {
    estado = 1;
} else if (month28.includes(monthUnknown)) {
    estado = 2;
} else {
    estado = 3;
}

switch (estado){
    case 1:
        console.log("El mes de", monthUnknown, "tiene 31 dias");
        break;
    case 2:
        console.log("El mes de", monthUnknown, "tiene 28 dias");
        break;
    case 3:
        console.log("El mes de", monthUnknown, "tiene 30 dias");
        break;
}
