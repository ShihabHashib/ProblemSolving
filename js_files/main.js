import { strangeCounter } from "./strangeCounter.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + strangeCounter(17);
