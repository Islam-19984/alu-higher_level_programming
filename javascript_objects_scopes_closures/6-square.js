#!/usr/bin/node

const parentSquared = require('./5-square');

class Square extends parentSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    const char = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width);
    }
  }
}

module.exports = Square;
