#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;

if (arg.length <= 3) {
  console.log(0);
} else {
  let newList = [];
  for (let index = 2; index < arg.length; index++) {
    newList.push(arg[index]);
  }
  newList = newList.sort().reverse().map(Number);
  console.log(newList[1]);
}
