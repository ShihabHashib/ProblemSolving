// Minimum Number Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function minimumNumber(n, password) {
  let minNumber = 0;

  if (n <= 3) return 6 - n;
  if (password.match(/\d/) === null) minNumber++;
  if (password.match(/[A-Z]/) === null) minNumber++;
  if (password.match(/[a-z]/) === null) minNumber++;
  if (password.match(/\W/) === null) minNumber++;

  const result = minNumber + n >= 6 ? minNumber : 6 - n;
  return result;
}
