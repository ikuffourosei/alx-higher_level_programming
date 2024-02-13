#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;
if (arg[2] != null) {
  console.log(arg[2]);
} else {
  console.log('No argument');
}
