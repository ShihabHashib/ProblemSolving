// Angry Professor Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function angryProfessor(k, a) {
  let onTimeStudent = 0;

  for (const i in a) {
    if (a[i] <= 0) {
      console.log(a[i]);
      onTimeStudent++;
    }
  }

  const isCanceled = onTimeStudent >= k ? "NO" : "YES";

  return isCanceled;
}
