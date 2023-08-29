// Utopian Tree Javascript HackerRank Solution

// Remove Export if you want to paste in HackerRank
export function utopianTree(n) {
  let height = 0;
  for (let i = 0; i <= n; i++) {
    if (i % 2 == 0) {
      height++;
    } else {
      height *= 2;
    }
  }
  return height;
}
