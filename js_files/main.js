import { pangrams } from "./pangrams.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " +
  pangrams("We promptly judged antique ivory buckles for the next prize");
