// Equalize Array Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function equalizeArray(arr) {
  let mode;
  let maxCount = 0;
  const numCounts = {};

  for (const num of arr) {
    if (num in numCounts) {
      numCounts[num]++;
    } else {
      numCounts[num] = 1;
    }
  }

  // Find most frequent number
  for (const num in numCounts) {
    if (numCounts[num] > maxCount) {
      mode = num;
      maxCount = numCounts[num];
    }
  }
  const deletionsNeeded = arr.length - maxCount;

  return deletionsNeeded;
}
