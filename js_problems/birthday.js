// Subarray Division Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function birthday(s, d, m) {
  let countItem = 0;

  for (var i = 0; i < s.length; i++) {
    let arrLength = s.slice(i, i + m);
    const sum = arrLength.reduce((a, b) => a + b, 0);
    if (sum === d) {
      countItem++;
    }
  }

  return countItem;
}
