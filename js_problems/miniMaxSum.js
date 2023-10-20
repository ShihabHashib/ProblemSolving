// Mini Max Sum Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function miniMaxSum(arr) {
  let max = arr.reduce((a, b) => Math.max(a, b));
  let min = arr.reduce((a, b) => Math.min(a, b));

  let sum = arr.reduce((a, b) => a + b);

  console.log(sum - max, sum - min);
}
