// Divisible Sum Pairs Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function divisibleSumPairs(n, k, ar) {
  let pairs = 0;

  for (var i = 0; i <= ar.length; i++) {
    for (var j = i + 1; j <= ar.length; j++) {
      if ((ar[i] + ar[j]) % k == 0) {
        pairs++;
      }
    }
  }
  return pairs;
}
