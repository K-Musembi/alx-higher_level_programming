#!/usr/bin/node

const cmd = require('process');
const args = cmd.argv;
let num;

if (args.length >= 3) {
  num = Number(args[2]);
}

if (args.length < 3 || isNaN(num)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
