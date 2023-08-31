// Beautiful Days at the Movies Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function beautifulDays(i, j, k) {
  let countBeautiful = 0;
  for (let a = i; a <= j; a++) {
    let reverse = a.toFixed(0).split("").reverse().join("") - 0;
    let isBeautiful = ((a - reverse) / k) % 1 != 0 ? false : true;
    if (isBeautiful) countBeautiful++;
  }
  return countBeautiful;
}
