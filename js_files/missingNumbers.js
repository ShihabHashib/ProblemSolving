// Missing Numbers Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function missingNumbers(arr, brr) {
  const arrMap = new Map();

  for (const num of arr) {
    arrMap.set(num, (arrMap.get(num) || 0) + 1);
  }

  const missingNumbers = [];

  for (const num of brr) {
    if (!arrMap.has(num) || arrMap.get(num) === 0) {
      missingNumbers.push(num);
    } else {
      arrMap.set(num, arrMap.get(num) - 1);
    }
  }

  const accOrder = [...new Set(missingNumbers)].sort((a, b) => a - b);

  return accOrder;
}
