import { fairRations } from "./fairRations.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + fairRations([2, 3, 4, 5, 6]);
