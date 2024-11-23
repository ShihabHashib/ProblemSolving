"use strict";
// 771. Jewels and Stones
var numJewelsInStones = function (jewels, stones) {
  const j = [...jewels];
  const s = [...stones];

  const count = s.filter((i) => j.includes(i)).length;
  return count;
};
// For Displaying in HTML file ==========
var numJewelsInStones_2535 = function () {
  var jewels = "aA",
    stones = "aAAbbbb";
  var display = numJewelsInStones(jewels, stones);
  var showResult = document.querySelector(".app");
  showResult.innerHTML = "This is result: " + display;
};
numJewelsInStones_2535();
