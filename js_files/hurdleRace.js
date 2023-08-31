// Simple Array Sum Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function hurdleRace(k, height) {
  let count = 0;
  let newArray = [];
  let maxCount;
  for (const i in height) {
    if (height[i] > k) {
      count = height[i] - k;
      newArray.push(count);
    }
  }

  console.log(newArray);

  if (newArray.length === 0) {
    maxCount = 0;
  } else {
    maxCount = Math.max(...newArray);
  }

  return maxCount;
}
