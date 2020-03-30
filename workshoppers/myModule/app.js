'use strict';

const Enigma = require('./enigma');     // Since index.js is now returning a Constructor
const eng = new Enigma('magrathea');

let encodeString = eng.encode("Don't Panic!");
let decodeString = eng.decode(encodeString);

console.log("Encoded: ", encodeString);
console.log("Decoded: ", decodeString);

let qr = eng.qrgen("http://npmjs.com", "outImage.png");

qr ? console.log('QR Code Created!') : console.log("GR Code Creation Failed");





// console.log(eng.hello("Dave"));
// console.log(eng.goodmorning("Lisa"));
// const enigma = require('./enigma');
// console.log(enigma.hello("Dave"));