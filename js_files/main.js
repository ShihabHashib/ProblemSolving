import { camelcase } from "./camelcase.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + camelcase("saveChangesInTheEditor");
