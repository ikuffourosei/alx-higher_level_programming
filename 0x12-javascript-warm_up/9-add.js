#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;

function add (a, b) {
  if (!isNaN(a) && !isNaN(b)) {
    const num1 = parseInt(a);
    const num2 = parseInt(b);
    return (num1 + num2);
  } else {
    return NaN;
  }
}

const firstDigit = arg[2];
const lastDigit = arg[3];
const result = add(firstDigit, lastDigit);
console.log(result);
