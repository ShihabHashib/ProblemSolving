// Find Digits Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function findDigits(n) {
  let divisorCount = 0;
  const divisors = String(n).split("");
  for (const i of divisors) {
    if (n % i == 0) divisorCount++;
  }
  return divisorCount;
}
