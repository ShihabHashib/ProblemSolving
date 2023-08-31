// Bill Division Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function bonAppetit(bill, k, b) {
  let text;
  let newBill = bill.splice(k, 1);
  let eachShouldPaid = bill.reduce((a, b) => a + b, 0) / 2;

  if (eachShouldPaid == b) {
    text = "Bon Appetit";
  } else {
    text = Math.abs(b - eachShouldPaid);
  }

  console.log(text);
}
