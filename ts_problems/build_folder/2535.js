"use strict";
// 2535. Difference Between Element Sum and Digit Sum of an Array
var differenceOfSum = function (nums) {
    var sumOfArr = nums.reduce(function (a, b) { return a + b; }, 0);
    var sumOfDigits = nums.reduce(function (sum, num) {
        var digits = num.toString().split('').map(Number);
        return sum + digits.reduce(function (digitSum, digit) { return digitSum + digit; }, 0);
    }, 0);
    return sumOfArr - sumOfDigits;
};
// For Displaying in HTML file ========== 
var displayResult_2535 = function () {
    var nums = [1, 15, 6, 3];
    var display = differenceOfSum(nums);
    var showResult = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
};
displayResult_2535();
