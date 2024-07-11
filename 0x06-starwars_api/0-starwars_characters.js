#!/usr/bin/node

const request = require('request');

const fetchCharacters = (movieId) => {
  const baseUrl = `https://swapi.dev/api/films/${movieId}/`;
//	const baseUrl = `https://swapi-api.hbtn.io/api/`;

  request(baseUrl, (error, response, body) => {
    if (error) throw error;
    if (response.statusCode == 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;
      exactOrder(characterUrls, 0);
    } else {
      console.error(`Failed to fetch movie data for movie ID ${movieId}`);
    }
  });
};

const exactOrder = (actors, index) => {
  if (index === actors.length) return;
  request(actors[index], (error, response, body) => {
    if (error) throw error;
    if (response.statusCode == 200) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      exactOrder(actors, index + 1);
    } else {
      console.error(`Failed to fetch character data from ${actors[index]}`);
    }
  });
};

if (process.argv.length !== 3) {
  console.error('Usage: <movie_id>');
} else {
  const movieId = process.argv[2];
  fetchCharacters(movieId);
}
