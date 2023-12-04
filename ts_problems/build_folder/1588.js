"use strict";
// 1588. Sum of All Odd Length Subarrays
var sumOddLengthSubarrays = function (arr) {
    var len = arr.length;
    var total = 0;
    for (var i = 0; i < len; i++) {
        total += arr[i] * (Math.floor((i + 1) / 2) * Math.floor((len - i) / 2) +
            Math.ceil((i + 1) / 2) * Math.ceil((len - i) / 2));
    }
    return total;
};
// For Displaying in HTML file ========== 
var sumOddLengthSubarrays_2535 = function () {
    var arr = [1, 4, 2, 5, 3];
    var display = sumOddLengthSubarrays(arr);
    var showResult = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
};
sumOddLengthSubarrays_2535();
