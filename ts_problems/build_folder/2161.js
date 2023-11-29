"use strict";
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
// 2161. Partition Array According to Given Pivot
var pivotArray = function (nums, pivot) {
    var left = [];
    var right = [];
    var center = [];
    for (var i = 0; i < nums.length; i++) {
        if (nums[i] < pivot)
            left.push(nums[i]);
        else if (nums[i] > pivot)
            right.push(nums[i]);
        else
            center.push(nums[i]);
    }
    return __spreadArray(__spreadArray(__spreadArray([], left, true), center, true), right, true);
};
// For Displaying in HTML file ========== 
var displayResult_2161 = function () {
    var nums = [9, 12, 5, 10, 14, 3, 10];
    var pivot = 10;
    var display = pivotArray(nums, pivot);
    var showResult = document.querySelector(".app");
    showResult.innerHTML = "This is result: " + display;
};
displayResult_2161();
