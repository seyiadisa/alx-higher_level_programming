#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    let char = c;

    if (char === undefined) {
      char = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(char.repeat(this.size));
    }
  }
}

module.exports = Square;
