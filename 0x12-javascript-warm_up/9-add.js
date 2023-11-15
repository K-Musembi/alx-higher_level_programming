#!/usr/bin/node

const cmd = require('process');
const args = cmd.argv;

function add(a, b) {
  return a + b;
}

console.log(add(Number(args[2]), Number(args[3])));
