#!/usr/bin/node
const { argv } = require('process');
const iterations = Number(argv[2]);
const display = () => {
  for (let i = 0; i < iterations; i++) {
    console.log('C is fun');
  }
};
if (isNaN(iterations)) { console.log('Missing number of occurences'); } else {
  display();
}
