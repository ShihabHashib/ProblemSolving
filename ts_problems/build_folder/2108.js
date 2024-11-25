"use strict";
// 2108. Find First Palindromic String in the Array
var firstPalindrome = function (words) {
  const result = words.find(
    (word) => word === word.split("").reverse().join("")
  );
  return result || "";
};
// For Displaying in HTML file ==========
var firstPalindrome_Show = function () {
  var words = ["abc", "car", "ada", "racecar", "cool"];
  var display = firstPalindrome(words);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
firstPalindrome_Show();
