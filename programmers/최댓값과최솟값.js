function solution(s) {
  const li = s.split(" ");
  const parsedLi = li.map((l) => {
    return parseInt(l);
  });
  const mini = Math.max.apply(null, parsedLi);
  const maxi = Math.min.apply(null, parsedLi);
  return maxi + " " + mini;
}
