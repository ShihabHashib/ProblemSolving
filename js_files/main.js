import { bigSorting } from "./bigSorting.js";
const showResult = document.querySelector(".app");

const arr = [
  8, 1, 2, 100, 12303479849857341718340192371, 3084193741082937,
  3084193741082938, 111, 200,
];

showResult.innerHTML = "This is result: " + bigSorting(arr);
