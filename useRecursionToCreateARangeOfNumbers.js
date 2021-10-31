function useRecursionToCreateARangeOfNumbers(startNum, endNum, result = []) {
  if(startNum === endNum) {
    result.push(startNum)
    return result
  }
  result = useRecursionToCreateARangeOfNumbers(startNum, endNum - 1, result)
  result.push(endNum)
  return result;
};

console.log(useRecursionToCreateARangeOfNumbers(10, 23))