import { chocolateFeast } from "./chocolateFeast.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + chocolateFeast(15, 3, 2);
