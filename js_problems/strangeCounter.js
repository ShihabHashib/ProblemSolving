// Strange Counter Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function strangeCounter(t) {
  let startingTime = 1;
  let cycleLength = 3;

  while (t > startingTime + cycleLength - 1) {
    startingTime += cycleLength;
    cycleLength *= 2;
  }

  const value = cycleLength - (t - startingTime);

  return value;
}
