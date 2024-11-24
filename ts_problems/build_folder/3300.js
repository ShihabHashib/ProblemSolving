"use strict";
// 3300. Minimum Element After Replacement With Digit Sum
var minElement = function (nums) {
  return Math.min(
    ...nums.map((num) =>
      num
        .toString()
        .split("")
        .reduce((sum, digit) => sum + Number(digit), 0)
    )
  );
};
// For Displaying in HTML file ==========
var minElement_Show = function () {
  var nums = [10, 12, 13, 14];
  var display = minElement(nums);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
minElement_Show();
