const fs = require("fs");

let input = fs.readFileSync("/dev/stdin").toString().split("-");
let answer = input.reduce((total, item, idx) => {
  let sum = item
    .split("+")
    .map((a) => parseInt(a))
    .reduce((total, cur) => total + cur, 0);

  return idx === 0 ? total + sum : total - sum;
}, 0);

console.log(answer);
