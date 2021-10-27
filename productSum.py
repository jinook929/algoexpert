def productSum(array, depth = 0):
  result = 0
  depth += 1
  # check the array if it has arrays as item
  # if the current list does not have any inner lists, add all num items and multiply it by depth.
  if not findList(array):
    tmpsum = 0
    for i in array:
      tmpsum += i
    return tmpsum * depth
  # if not... distinguish items between int and list
  for item in array:
    # if int, add to result
    if type(item) == int:
      result += item
    # if list, execute this function recursively and update result with it
    else:
      result += productSum(item, depth)
  # return result value timed by depth
  return result * depth

def findList(mylist):
  for item in mylist:
    if type(item) == list:
      return True
  return False

# print(findList([1,2,3]))
# print(findList([1,[2,3]]))

# print(productSum([1,[2,3]])) #=> 11
# print(productSum([1,[2,3],4,[5,[6,7]],8,[9],10])) #=> 139 = 15+88+8+18+10
# print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])) #=> 12
print(productSum([1,[2,[3]]])) #=> 23