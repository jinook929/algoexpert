function useRecursionToCreateACountdown(n, result = []){
  if (n < 1) return result
  result.push(n)
  useRecursionToCreateACountdown(n - 1, result)
  return result;
}

console.log(useRecursionToCreateACountdown(10))