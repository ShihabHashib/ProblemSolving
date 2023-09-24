// Library Fine Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function libraryFine(d1, m1, y1, d2, m2, y2) {
  let fines = 0;
  const years = y1 - y2;
  const months = m1 - m2;
  const days = d1 - d2;

  const date1 = new Date(y1, m1, d1);
  const date2 = new Date(y2, m2, d2);

  if (date1 < date2) return 0;
  else if (years > 0) fines = 10000;
  else if (years == 0 && months > 0) fines = 500 * months;
  else fines = 15 * days;

  return fines;
}
