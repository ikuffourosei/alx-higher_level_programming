#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;

if (arg.length <= 3) {
  console.log(0);
} else {
  let newList = arg.slice(2).map(Number);
  newList = newList.sort((a, b) => b - a);
  console.log(newList[1]);
}
