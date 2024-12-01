"use strict";
// 3289. The Two Sneaky Numbers of Digitville
var getSneakyNumbers = function (nums) {
  const counts = {};

  for (const num of nums) {
    counts[num] = counts[num] ? counts[num] + 1 : 1;
  }

  const result = Object.entries(counts)
    .filter(([key, value]) => value > 1)
    .map(([key]) => Number(key));

  return result;
};
// For Displaying in HTML file ==========
var getSneakyNumbers_2535 = function () {
  var nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2];
  var display = getSneakyNumbers(nums);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
getSneakyNumbers_2535();
