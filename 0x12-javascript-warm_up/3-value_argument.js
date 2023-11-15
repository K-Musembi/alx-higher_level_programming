#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.includes(3)) {
  let arg = args[2];
  console.log(arg);
} else {
  console.log('No argument');
}
