// Chocolate Feast Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function chocolateFeast(n, c, m) {
  let choPackage = Math.floor(n / c);
  let numOfCho = choPackage;
  let addCho;

  while (choPackage >= m) {
    addCho = Math.floor(choPackage / m);
    choPackage -= addCho * m;
    choPackage += addCho;
    numOfCho += addCho;
  }

  return numOfCho;
}
