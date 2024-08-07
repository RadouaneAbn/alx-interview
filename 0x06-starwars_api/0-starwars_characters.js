#!/usr/bin/node
const request = require('request');

function get (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (err, res, body) => {
      if (err) {
        console.error('Err:', err);
        reject(err);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function retriveCharacters (url) {
  const data = await get(url);
  for (const user of data.characters) {
    const name = await getCharInfo(user);
    console.log(name);
  }
}

async function getCharInfo (url) {
  const user = await get(url);
  return (user.name);
}

function main () {
  const movieId = process.argv[2];
  retriveCharacters('https://swapi-api.alx-tools.com/api/films/' + movieId + '/');
}

main();
