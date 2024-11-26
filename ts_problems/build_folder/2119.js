"use strict";
// 2119. A Number After a Double Reversal
var isSameAfterReversals = function (num) {
  if ((num = 0)) return true;
  return num % 10 == 0 ? true : false;
};
// For Displaying in HTML file ==========
var isSameAfterReversals_Show = function () {
  var num = 526;
  var display = isSameAfterReversals(num);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
isSameAfterReversals_Show();
