function fileName(str) {
  return str.split(" ").map((word, i) => i > 0 ? word[0].toUpperCase() + word.slice(1) : word[0].toLowerCase() + word.slice(1)).join("")
}

console.log(fileName("Use Recursion to Create a Countdown"))