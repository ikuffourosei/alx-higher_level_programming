#!/usr/bin/node

const processArg = require('process');
const arg = processArg.argv;

if (!isNaN(arg[2])) {
  const num = parseInt(arg[2]);
  console.log(`My number: ${num}`);
} else {
  console.log('Not a number');
}
