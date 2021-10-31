function replaceLoopsUsingRecursion(arr, n, result = 0) {
  // Only change code below this line

  // let i = 0
  // while (i < n) {
  //   result += arr[i]
  //   i++
  // }
  
  if (n === 0) return 0
  result += arr[n - 1] + replaceLoopsUsingRecursion(arr, n - 1, result)
  return result
  // Only change code above this line
}

console.log(replaceLoopsUsingRecursion([2, 3, 4, 5], 3))