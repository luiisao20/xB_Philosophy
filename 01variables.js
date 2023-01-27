var cajaA = 3;
cajaA = 7;
var cajaB = 5;
var cajaC = cajaA + cajaB;

console.log(cajaA, cajaB, "La suma es", cajaC);

var x = 2;
var y = 3;
console.log(x, y);
// Intercambiar valores de x e y
// c = x;
// x = y;
// y = c;
[x, y] = [y, x];
console.log(x, y);