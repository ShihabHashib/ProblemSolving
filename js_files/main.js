import { equalizeArray } from "./equalizeArray.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + equalizeArray([3, 3, 2, 1, 3]);
