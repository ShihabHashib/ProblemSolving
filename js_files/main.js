import { beautifulTriplets } from "./beautifulTriplets.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " + beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]);
