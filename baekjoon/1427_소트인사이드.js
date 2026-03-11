const fs = require("fs");

let input = fs.readFileSync("/dev/stdin").toString().split("\n");
// fs.readFileSync("/dev/stdin").toString();

console.log(
  input[0]
    .split("")
    .map(Number)
    .sort((a, b) => b - a)
    .join("")
);
