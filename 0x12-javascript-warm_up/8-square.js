#!/usr/bin/node
const { argv } = require('process');
const size = Number(argv[2]);
const repeat = 'X'.repeat(size);
const printSquare = () => {
  for (let i = 0; i < size; i++) {
    console.log(repeat);
  }
};
if (isNaN(size)) {
  console.log('Missing size');
} else { printSquare(); }
