#!/usr/bin/node

const process = require('process');
const request = require('request');

let url = process.argv[2];
url = 'https://swapi-api.alx-tools.com/people/18';

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const arr = body.films;
  console.log(arr.length);
});
