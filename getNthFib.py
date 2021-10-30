memo = {}

def getNthFib(num):
    if num <= 2:
        return num - 1

    # return getNthFib(num - 1) + getNthFib(num - 2)

    # if num in memo:
    #     return memo[num]
    # else:
    #     memo[num] = getNthFib(num - 1) + getNthFib(num - 2)
    #     return memo[num]

    # if num not in memo:
    #     memo[num] = getNthFib(num - 1) + getNthFib(num - 2)
    # return memo[num]

    # numsList = [0, 1]
    # for i in range(2, num):
    #     numsList.append(numsList[i - 1] + numsList[i - 2])
    # return numsList[len(numsList) - 1]

    numsList = [0, 1]
    for i in range(2, num):
        numsList = [numsList[1], numsList[0] + numsList[1]]
    return numsList[1]

print(getNthFib(1))
print(getNthFib(2))
print(getNthFib(3))
print(getNthFib(4))
print(getNthFib(5))
print(getNthFib(6))
print(getNthFib(7))
print(getNthFib(8))
print(getNthFib(9))
print(getNthFib(10))
print(getNthFib(50))
print(getNthFib(100))