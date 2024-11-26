"use strict";
// 3131. Find the Integer Added to Array I
var addedInteger = function (nums1, nums2) {
  return Math.min(...nums2) - Math.min(...nums1);
};
// For Displaying in HTML file ==========
var addedInteger_Show = function () {
  var nums1 = [2, 6, 4],
    nums2 = [9, 7, 5];
  var display = addedInteger(nums1, nums2);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
addedInteger_Show();
