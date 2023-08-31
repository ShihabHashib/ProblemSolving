// Counting Valleys Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function countingValleys(steps, path) {
  let seaLevel = 0;
  let valley = 0;
  let isValley = false;
  let singlePath = path.split("");

  singlePath.forEach((step) => {
    step === "U" ? seaLevel++ : seaLevel--;
    if (seaLevel < 0 && !isValley) {
      valley++;
      isValley = true;
    } else if (seaLevel >= 0 && isValley) {
      isValley = false;
    }
  });
  return valley;
}
