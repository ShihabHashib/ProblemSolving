// Super Reduced String Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function superReducedString(s) {
  const charecters = [];

  for (const char of s) {
    if (charecters.length > 0 && charecters[charecters.length - 1] === char)
      charecters.pop();
    else {
      charecters.push(char);
    }
  }

  if (charecters.length === 0) {
    return "No string";
  }

  const reducedStr = charecters.join("");

  return reducedStr;
}
