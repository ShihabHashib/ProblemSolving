// Remove Export if you want to paste in HackerRank
export function designerPdfViewer(h, word) {
  const data = [];
  const valueArray = [];
  const keys = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];
  const wordInArray = word.split("");

  keys.forEach((key, i) => (data[key] = h[i]));

  for (const key of wordInArray) {
    if (data.hasOwnProperty(key)) {
      valueArray.push(data[key]);
    }
  }

  const max = Math.max(...valueArray);
  const count = valueArray.length;
  const area = max * count;

  return area;
}
