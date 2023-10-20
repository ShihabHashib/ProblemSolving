// Gemstones Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function gemstones(arr) {
  if (arr.length === 0) {
    return [];
  }

  const firstWordChars = arr[0].split("");

  const commonChars = firstWordChars.filter((char) => {
    return arr.every((word) => word.includes(char));
  });

  return [...new Set(commonChars)];
}
