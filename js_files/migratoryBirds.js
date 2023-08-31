// Migratory Birds Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function migratoryBirds(arr) {
  let nums = {};
  let max = 0;
  let n;

  for (let i in arr) {
    nums[arr[i]] = (nums[arr[i]] || 0) + 1;
    if (nums[arr[i]] > max) {
      max = nums[arr[i]];
      n = arr[i];
    }
  }

  let item = [];
  for (let i in nums) {
    if (nums[i] == max) {
      item.push(i);
    }
  }

  let result = Math.min(...item);

  return result;
}
