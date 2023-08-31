// Sales by Match Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function sockMerchant(n, ar) {
  let socks = {};
  let pairs = 0;
  for (let i of ar) {
    socks[i] = socks[i] + 1 || 1;
    if (socks[i] % 2 === 0) {
      pairs += 1;
    }
  }

  return pairs;
}
