function solution(n) {
  if (n % 2 === 1) return 2;
  for (let i = 3; i < n - 1; i++) {
    if (n % i == 1) return i;
  }
  return n - 1;
}
