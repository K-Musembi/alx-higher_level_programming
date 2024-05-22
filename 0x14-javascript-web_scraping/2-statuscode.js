#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log('code: ', response.statusCode);
});
