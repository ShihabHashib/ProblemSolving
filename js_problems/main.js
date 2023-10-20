import { beautifulBinaryString } from "./beautifulBinaryString.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + beautifulBinaryString("0101010");
