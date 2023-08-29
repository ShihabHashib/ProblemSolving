import { plusMinus } from "./plusMinus.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + plusMinus([0, 0, -1, 1, 1]);
