// Hackerrank In String Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function hackerrankInString(s) {
  const target = "hackerrank";
  for (const char of target) {
    if (s.indexOf(char) === -1) {
      return "NO";
    }
    console.log(s, s.indexOf(char));
    s = s.slice(s.indexOf(char) + 1);
  }
  return "YES";
}
