import { howManyGames } from "./howManyGames.js";
const showResult = document.querySelector(".app");

showResult.innerHTML = "This is result: " + howManyGames(99, 3, 1, 5555);
