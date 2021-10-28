# def productSum(array, depth = 0):
#   total = 0
#   depth += 1
#   for item in array:
#     if type(item) == int:
#       total += item
#     else:
#       total += productSum(item, depth)
#   return total * depth

# print(findList([1,2,3]))
# print(findList([1,[2,3]]))

def productSum(array, depth = 1):
    total = 0
    for item in array:
        if type(item) == int:
            total += item
        else:
            total += productSum(item, depth + 1)
    return total * depth

# print(productSum([1,[2,3]])) #=> 11
# print(productSum([1,[2,3],4,[5,[6,7]],8,[9],10])) #=> 139 = 15+88+8+18+10
# print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])) #=> 12
print(productSum([1,[2,[3]]])) #=> 23