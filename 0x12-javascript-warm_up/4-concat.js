#!/usr/bin/node
const processArg = require('process');
const arg = processArg.argv;
const len = arg.length;
if (len != null) {
  console.log(`${arg[2]} is ${arg[3]}`);
}
