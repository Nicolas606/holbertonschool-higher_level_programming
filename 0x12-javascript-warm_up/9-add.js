#!/usr/bin/node
const argument = process.argv;
const first = parseInt(argument[2], 10);
const second = parseInt(argument[3], 10);
function add (a, b) {
  return a + b;
}
console.log(add(first, second));
