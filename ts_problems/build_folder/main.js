"use strict";
// 2161. Partition Array According to Given Pivot
var funcName = function (num) {
    return num;
};
// For Displaying in HTML file ========== 
var displayResult = function () {
    var num = [5, 6, 6, 7, 2];
    var display = funcName(num);
    var showResult = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
};
displayResult();
