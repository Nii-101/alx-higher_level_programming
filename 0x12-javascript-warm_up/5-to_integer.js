#!/usr/bin/node
const { argv } = require('process');
const convertArg = Number(argv[2]);
if (isNaN(convertArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertArg);
}
