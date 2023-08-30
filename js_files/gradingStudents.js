// Grading Students Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function gradingStudents(grades) {
  for (let i = 0; i < grades.length; i++) {
    let round = Math.ceil(grades[i] / 5) * 5;

    if (grades[i] >= 38 && round - grades[i] < 3) {
      grades[i] = round;
    }
  }

  return grades;
}
