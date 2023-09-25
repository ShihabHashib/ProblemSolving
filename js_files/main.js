import { saveThePrisoner } from "./saveThePrisoner.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " + saveThePrisoner(352926151, 380324688, 94730870);
