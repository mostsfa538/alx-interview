#!/usr/bin/node

const request = require('request')
const movieId = process.argv[2]
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;
  characters.forEach(charactersUrl => {
    request(charactersUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const charactersData = JSON.parse(body);
      console.log(charactersData.name)
    })
  });
});
