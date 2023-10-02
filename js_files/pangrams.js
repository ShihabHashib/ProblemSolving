// Pangrams Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function pangrams(s) {
  let count = 0;
  let arr = [];
  let isPangram = "";
  const lowerStr = s.toLowerCase();

  for (const char of lowerStr) {
    if (char.match(/[a-z]/) && !arr.includes(char)) {
      arr.push(char);
      count++;
    }
  }

  if (count == 26) {
    isPangram = "pangram";
  } else {
    isPangram = "not pangram";
  }

  console.log(count, arr.sort());
  return isPangram;
}
