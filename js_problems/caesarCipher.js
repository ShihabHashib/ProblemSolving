// Caesar Cipher Javascript HackerRank Solution

// Remove 'export' if you want to paste in HackerRank
export function caesarCipher(s, k) {
  const lowAlph = "abcdefghijklmnopqrstuvwxyz";
  const upperAlph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  let result = "";

  for (let i = 0; i < s.length; i++) {
    let char = s[i];

    if (lowAlph.includes(char)) {
      const newIndex = (lowAlph.indexOf(char) + k) % lowAlph.length;
      result += lowAlph[newIndex];
    } else if (upperAlph.includes(char)) {
      const newIndex = (upperAlph.indexOf(char) + k) % upperAlph.length;
      result += upperAlph[newIndex];
    } else {
      result += char;
    }
  }

  return result;
}
