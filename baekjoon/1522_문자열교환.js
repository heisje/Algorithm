const main = (st) => {
  const arr = [...st];

  let i = 0;
  let a = {};
  let aIdx = 0;
  let b = {};
  let bIdx = 0;
  while (i < arr.length) {
    if (arr[i] === "a") {
      a[aIdx++] = i;
    } else if (arr[i] === "b") {
      b[bIdx++] = i;
    }
    i++;
  }
  
  console.log(a);
  console.log(b);
};

main("ba");
main("aaaabbbbba");
