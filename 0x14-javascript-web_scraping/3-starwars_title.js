#!/usr/bin/node

const process = require('process');
const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, { json: true }, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  console.log(body.title);
});
