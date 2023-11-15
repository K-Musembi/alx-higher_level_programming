#!/usr/bin/node

const cmd = require('process');
const args = cmd.argv;
const num = Number(args[2]);

function factorial (n) {
  if (isNaN(n) || n <= 1) {
	  return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(num));
