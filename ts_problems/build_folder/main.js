"use strict";
// Problem Name
var funcName = function (num) {
    return num;
};
var num = [5, 6, 6, 7, 2];
var display = funcName(num);
// For Displaying in HTML file ========== 
// Don't have to edit this, change file name on index-ts.html
var showResult = document.querySelector(".app");
showResult.innerHTML = "This is result: " + display;
