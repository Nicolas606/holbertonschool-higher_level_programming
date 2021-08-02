#!/usr/bin/node
const argument = process.argv;
const num = parseInt(argument[2], 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
