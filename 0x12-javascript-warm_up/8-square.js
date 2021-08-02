#!/usr/bin/node
const argument = process.argv;
const num = parseInt(argument[2], 10);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let n = 0; n < num; n++) {
    console.log('X'.repeat(num));
  }
}
