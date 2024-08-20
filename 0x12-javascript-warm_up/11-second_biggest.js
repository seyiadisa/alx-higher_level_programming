#!/usr/bin/node
const { argv } = require('node:process');

const args = argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const secondLargest = args.sort((a, b) => b - a);
  console.log(secondLargest[1]);
}
