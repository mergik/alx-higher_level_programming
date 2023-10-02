#!/usr/bin/node
const Square = require('./5-square');

class SquareCharPrint extends Square {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = SquareCharPrint;