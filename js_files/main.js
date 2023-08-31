import { beautifulDays } from "./beautifulDays.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + beautifulDays(20, 23, 6);
