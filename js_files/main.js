import { superReducedString } from "./superReducedString.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + superReducedString("aaabccdddd");
