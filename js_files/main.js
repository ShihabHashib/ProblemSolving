import { missingNumbers } from "./missingNumbers.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " +
  missingNumbers(
    [203, 204, 205, 206, 207, 208, 203, 204, 205, 206],
    [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
  );
