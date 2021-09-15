#!/usr/bin/node
/* script that writes a string to a file. */

const fs = require('fs');
const archivo = process.argv[2];
const data = process.argv[3];

fs.writeFile(archivo, data, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
