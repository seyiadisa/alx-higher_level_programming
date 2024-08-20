#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  if (isNaN(n)) return 1;
  if (n === 0) return 1;

  return n * factorial(n - 1);
}

const n = parseInt(argv[2]);
console.log(factorial(n));
