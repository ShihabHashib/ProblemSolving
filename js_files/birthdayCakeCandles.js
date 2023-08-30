// Birthday Cake Candles Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function birthdayCakeCandles(candles) {
  let max = candles.reduce((a, b) => Math.max(a, b));
  // let min = arr.reduce((a, b) => Math.min(a, b));

  let maxCount = 0;

  for (let i = 0; i < candles.length; i++) {
    if (candles[i] == max) {
      maxCount++;
    }
  }
  return maxCount;
}
