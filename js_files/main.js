import { angryProfessor } from "./angryProfessor.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + angryProfessor(3, [-1, -3, 4, 2]);
