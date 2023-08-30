// Apple and Orange Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function countApplesAndOranges(s, t, a, b, apples, oranges) {
  let appleCount = 0;
  let orangeCount = 0;

  for (var i = 0; i < apples.length; i++) {
    let falDistance = a + apples[i];
    if (falDistance >= s && falDistance <= t) {
      appleCount++;
    }
  }

  for (var i = 0; i < oranges.length; i++) {
    let falDistance = b + oranges[i];
    if (falDistance >= s && falDistance <= t) {
      orangeCount++;
    }
  }

  console.log(appleCount);
  console.log(orangeCount);
}
