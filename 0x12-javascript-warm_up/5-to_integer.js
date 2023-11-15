#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (args.length >= 3) {
  const num = Number(args[2]);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + num);
  }
} else {
  console.log('Not a number');
}
