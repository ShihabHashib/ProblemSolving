// Permutation Equation Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function permutationEquation(p) {
  const valueArr = [];

  for (let x = 1; x <= p.length; x++) {
    const y = p.indexOf(x) + 1;
    const z = p.indexOf(y) + 1;
    valueArr.push(z);
  }

  return valueArr;
}
