// Plus Minus Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function plusMinus(arr) {
  let neg = 0;
  let pos = 0;
  let zero = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      pos++;
    }
    if (arr[i] < 0) {
      neg++;
    }
    if (arr[i] == 0) {
      zero++;
    }
  }

  let negRa = neg / arr.length;
  let posRa = pos / arr.length;
  let zeroRa = zero / arr.length;

  console.log(posRa.toFixed(6));
  console.log(negRa.toFixed(6));
  console.log(zeroRa.toFixed(6));
}
