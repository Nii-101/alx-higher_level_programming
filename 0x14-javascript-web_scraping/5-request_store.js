#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const link = process.argv[2];
const storePath = process.argv[3];

request(link).pipe(fs.createWriteStream(storePath));
