import { findDigits } from "./findDigits.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + findDigits(25);
