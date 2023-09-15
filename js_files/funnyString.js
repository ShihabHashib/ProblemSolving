// Funny String Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function funnyString(s) {
  const asciiArray = [...s].map((char) => char.charCodeAt(0));
  let j = asciiArray.length - 1;

  for (let i = 0; i < j; i++) {
    if (
      Math.abs(asciiArray[i] - asciiArray[i + 1]) !==
      Math.abs(asciiArray[j] - asciiArray[j - 1])
    )
      return "Not Funny";
    j--;
  }
  return "Funny";
}
