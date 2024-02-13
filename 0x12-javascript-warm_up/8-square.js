#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;
// checks if the input can be covnerted to a string
if (!isNaN(arg[2])) {
  const num = parseInt(arg[2]);
  for (let ind = 0; ind < num; ind++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
