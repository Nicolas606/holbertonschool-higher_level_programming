#!/usr/bin/node
/*  script that prints all characters of a Star Wars movie */

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

const request = require('request');
request(url, function (error, response) {
  if (error) {
    console.log(error);
  }
  const characters = (JSON.parse(response.body).characters);
  characters.forEach(element => {
    const people = element;
    request(people, function (error, response) {
      if (error) {
        console.log(error);
      }
      const result = (JSON.parse(response.body).name);
      console.log(result);
    });
  });
});
