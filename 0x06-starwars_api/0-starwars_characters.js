#!/usr/bin/node

const request = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/' + episodeNum;
let characters = [];

request(API_URL, async function (err, response, body) {
  if (err) {
    console.log(err);
  }
  characters = JSON.parse(body).characters;
  for (const c of characters) {
    await new Promise((resolve, reject) => {
      request(c, (err, res, body) => {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
