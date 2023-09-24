import { libraryFine } from "./libraryFine.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + libraryFine(2, 7, 1014, 1, 1, 1014);
