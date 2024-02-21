#!/usr/bin/node

const fs = require('fs');
const argument = process.argv[2];

fs.readFile(argument, 'utf-8', (err, content) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content.toString());
  }
});
