// Fair Rations Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function fairRations(B) {
  let arr = B;
  let loaves = 0;

  for (let i = 0; i < arr.length; i++) {
    while (arr[i] % 2 !== 0) {
      if (i === arr.length - 1) {
        return "NO";
      }
      arr[i]++;
      arr[i + 1]++;
      loaves += 2;
    }
  }

  return loaves;
}
