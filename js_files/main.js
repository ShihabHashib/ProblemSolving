import { caesarCipher } from "./caesarCipher.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " + caesarCipher("abcdefghijklmnopqrstuvwxyz", 2);
