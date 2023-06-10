#!/usr/bin/node
const Squared = require('./5-square');

module.export = class Square extends Squared {
  charprint (c) {
    if (c === underfined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
	s += c;
      }
      console.log(s);
    }
  }
};
