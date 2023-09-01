// Extra Long Factorials HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function extraLongFactorials(n) {
  let factorial = 1;
  for (let i = 1; i <= n; i++) {
    factorial = BigInt(factorial) * BigInt(i);
  }
  const factorialString = factorial.toString();
  console.log(factorialString);
}
