#!/usr/bin/node
const dictionary = require('./101-data').dict;
const newdict = {};
for (const key in dictionary) {
  newdict[dictionary[key]] = [];
}
for (const key in dictionary) {
  newdict[dictionary[key]].push(key);
}
console.log(newdict);
