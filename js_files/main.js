import { gemstones } from "./gemstones.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " + gemstones(["abcdde", "baccd", "eeabg"]);
