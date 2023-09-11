import { permutationEquation } from "./permutationEquation.js";
const showResult = document.querySelector(".app");

showResult.innerHTML =
  "This is result: " + permutationEquation([4, 3, 5, 1, 2]);
