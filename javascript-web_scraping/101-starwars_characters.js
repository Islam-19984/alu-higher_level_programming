#!/usr/bin/node
const request = require('request');

function fetchCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      return;
    }

    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
          return;
        }

        if (response.statusCode !== 200) {
          console.error('Invalid response:', response.statusCode);
          return;
        }

        const character = JSON.parse(body);
        console.log(character.name);
      });
    });
  });
}

fetchCharacters(3);
