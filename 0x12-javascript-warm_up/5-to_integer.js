#!/usr/bin/node
const arg = process.argv[2];
const parsedArg = parseInt(arg);

if (!isNaN(parsedArg)) {
  console.log(`My number: ${parsedArg}`);
} else {
  console.log('Not a number');
}
