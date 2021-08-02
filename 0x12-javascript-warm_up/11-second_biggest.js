#!/usr/bin/node
const argument = process.argv;

if (argument.length < 4) {
  console.log(0);
} else {
  const list = argument.sort(function (a, b) { return a - b; });
  console.log(list[(list.length) - (2)]);
}
