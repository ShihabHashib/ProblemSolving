// Number Line Jumps Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function kangaroo(x1, v1, x2, v2) {
  let kangaroo1 = x1 + v1;
  let kangaroo2 = x2 + v2;
  let getEqual = false;

  for (let i = 0; i <= 10000; i++) {
    if (kangaroo1 == kangaroo2) {
      getEqual = true;
      break;
    } else {
      kangaroo1 += v1;
      kangaroo2 += v2;
    }
  }

  let result = getEqual ? "YES" : "NO";

  return result;
}
