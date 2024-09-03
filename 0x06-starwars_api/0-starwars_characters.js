#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiURL, async (err, res, body) => {
  if (err && res.statusCode !== 200) {
    console.error(err);
    return;
  }

  const data = JSON.parse(body);

  for (const charURL of data.characters) {
    const responde = await doRequest(charURL);
    console.log(JSON.parse(responde).name);
  }
});

function doRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, function (err, res, body) {
      if (!err && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(err);
      }
    });
  });
}
