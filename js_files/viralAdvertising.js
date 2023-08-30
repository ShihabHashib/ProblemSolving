// Viral Advertising Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function viralAdvertising(n) {
  let people = 5;
  let totalLiked = 0;
  let likedEachDay = 0;

  for (let i = 1; i <= n; i++) {
    if (i > 1) {
      people *= 3;
    }
    likedEachDay = Math.floor(people / 2);
    people = likedEachDay;
    totalLiked += people;
  }
  return totalLiked;
}
