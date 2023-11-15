#!/usr/bin/node

const cmd = require('process');
const args = cmd.argv;

if (args.length < 3 || isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  let num = Number(args[2]);
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
}

