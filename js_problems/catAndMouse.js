// Cats and a Mouse Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function catAndMouse(x, y, z) {
  let text = "";
  const cataDis = Math.abs(z - x);
  const catbDis = Math.abs(z - y);

  if (cataDis < catbDis) {
    text = "Cat A";
  } else if (cataDis == catbDis) {
    text = "Mouse C";
  } else {
    text = "Cat B";
  }

  return text;
}
