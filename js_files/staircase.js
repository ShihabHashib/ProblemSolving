// Staircase Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function staircase(n) {
  let str;

  for (var i = 1; i <= n; i++) {
    console.log(" ".repeat(n - i) + "#".repeat(i));
  }
  return str;
}
