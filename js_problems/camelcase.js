// Camelcase Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function camelcase(s) {
  let count = 0;
  const upperCaseAlp = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
  ];

  for (const i of s) {
    if (upperCaseAlp.includes(i)) {
      count++;
    }
  }

  return count + 1;
}
