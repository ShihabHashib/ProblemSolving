// Electronics Shop Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function getMoneySpent(keyboards, drives, b) {
  let max = -1;

  let mixAmount = keyboards.flatMap((d) => drives.map((v) => d + v));

  for (const i in mixAmount) {
    if (mixAmount[i] <= b && mixAmount[i] > max) {
      max = mixAmount[i];
    }
  }
  return max;
}
