#!/usr/bin/node
/* script that reads and prints the content of a file */

const fs = require('fs');
const archivo = process.argv[2];

fs.readFile(archivo, 'utf8', (err, jsonString) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(jsonString);
});
