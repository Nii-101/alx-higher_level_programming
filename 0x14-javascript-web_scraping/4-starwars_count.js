#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) console.log('Error:', error);

  const films = JSON.parse(body).results;
  const wedgeFilms = films.filter(
    movies => movies.characters.find(character => character.match(/\/people\/18\/?$/))
  );
  console.log(wedgeFilms.length);
});
