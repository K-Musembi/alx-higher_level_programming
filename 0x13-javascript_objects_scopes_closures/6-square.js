#!/usr/bin/node

class Square extends require('./5-square') {

  constructor (size) {
    super (size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c) {
	  process.stdout.write(c);
	} else {
          process.stdout.write('X');
	}
      }
      process.stdout.write('\n');
    }
  }
}

module.exports = Square;
