#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;

function factorial (number) {
  if (!isNaN(number)) {
    const num = parseInt(number);
    if (num === 1) {
      return 1;
    } else {
      return num * (factorial(num - 1));
    }
  } else {
    return 1;
  }
}

const input = arg[2];
const result = factorial(input);
console.log(result);
