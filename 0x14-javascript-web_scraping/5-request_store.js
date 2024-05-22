#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const content = body;
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
