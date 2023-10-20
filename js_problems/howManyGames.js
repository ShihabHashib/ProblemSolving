// Halloween Sale Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function howManyGames(p, d, m, s) {
  let gameCount = 0;

  while (s >= p) {
    s -= p;
    p = p < m + d ? (p = m) : (p -= d);
    gameCount++;
  }
  return gameCount;
}

// howManyGames(p, d, m, s) {
//   let gameCount = 0;
//   let gameSum = 0;
//   let gamePrice = p;

//   while (gameSum < s - m) {
//     gameSum += gamePrice;
//     gamePrice = gamePrice < m + d ? (gamePrice = m) : (gamePrice -= d);
//     gameCount++;

//     console.log(gameCount, gamePrice, gameSum);
//   }
//   return gameCount;
// }
