const MLBFilter = require("multi-level-bloom-filter-js");
const LineByLine = require("n-readlines");

const REVOKED = 800000;
const UNREVOKED = 62000000;
const FP_RATE = 0.5;
const FP1_RATE = REVOKED * Math.sqrt(FP_RATE) / UNREVOKED;
const REVOKED_FILENAME = '../final_revoked.json';
const UNREVOKED_FILENAME = '../final_unrevoked.json';


let revoked  = []
let liner = new LineByLine(REVOKED_FILENAME);
let line;
while (line = liner.next()) {
  line = line.toString();
  revoked.push(line);
}

let unrevoked = ['test']
liner = new LineByLine(UNREVOKED_FILENAME);
while (line = liner.next()) {
  line = line.toString();
  unrevoked.push(line);
}

let mlbf = new MLBFilter(REVOKED, UNREVOKED, revoked, unrevoked, FP_RATE, FP1_RATE);
console.log(mlbf.toJSON());
