// Beautiful Binary String Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function beautifulBinaryString(b) {
  return (b.match(/010/g) || []).length;
}
