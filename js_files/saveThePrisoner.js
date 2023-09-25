// Save The Prisoner Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function saveThePrisoner(n, m, s) {
  return ((m - 1 + s - 1) % n) + 1;

  // let chair;
  // for (let i = 1; i <= m; i++) {
  //   chair = (i % n) + (s - 1);
  // }
  // return chair;
}
