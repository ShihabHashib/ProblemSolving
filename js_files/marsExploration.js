// Mars Exploration Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function marsExploration(s) {
  let errorCount = 0;
  for (let i = 0; i < s.length; i += 3) {
    if (s.charAt(i) != "S") errorCount++;
    if (s.charAt(i + 1) != "O") errorCount++;
    if (s.charAt(i + 2) != "S") errorCount++;
  }
  return errorCount;
}
