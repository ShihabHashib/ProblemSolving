// Breaking Records Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function breakingRecords(scores) {
  let arr = scores;

  let best = 0;
  let worst = 0;
  let numMax = arr[0];
  let numLow = arr[0];

  for (var i = 0; i < arr.length; i++) {
    if (arr[i] > numMax) {
      numMax = arr[i];
      best++;
    }
    if (arr[i] < numLow) {
      numLow = arr[i];
      worst++;
    }
  }

  return [best, worst];
}
