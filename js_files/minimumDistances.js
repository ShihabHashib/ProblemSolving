// Minimum Distances HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function minimumDistances(a) {
  const indexMap = {};
  let minDistance = Infinity;

  for (let i = 0; i < a.length; i++) {
    const num = a[i];

    if (indexMap[num] !== undefined) {
      const distance = i - indexMap[num];
      minDistance = Math.min(minDistance, distance);
    }

    indexMap[num] = i;
  }

  const result = minDistance === Infinity ? -1 : minDistance;

  return result;
}
