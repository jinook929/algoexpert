def sumOfNItems(arr, n, result = 0):
    # i = 0
    # while i < n:
    #     result += arr[i]
    #     i += 1
    if n == 0:
        return 0
    result += arr[n - 1] + sumOfNItems(arr, n - 1)
    return result

print("Replace Loops using Recursion :", sumOfNItems([2, 3, 4, 5], 3))