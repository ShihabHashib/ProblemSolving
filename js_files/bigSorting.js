// Big Sorting Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function bigSorting(unsorted) {
  let sortedArr = unsorted.sort((a, b) => {
    if (a.length == b.length) return a > b ? 1 : -1;
    return a.length - b.length;
  });
  return sortedArr;
}
