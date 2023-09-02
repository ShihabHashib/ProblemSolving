// Repeated String Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function repeatedString(s, n) {
  const count = (s.match(/a/g) || []).length * Math.floor(n / s.length);
  const remainderCount = n % s.length;
  const reminderMatch = (s.substring(0, remainderCount).match(/a/g) || [])
    .length;
  const TotalCount = count + reminderMatch;
  return TotalCount;
}
