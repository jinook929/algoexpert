def productSum(array):
  # Write your code here.
  result = 0
  # check the array if it has arrays as item
  
  # if the current list does not have any inner lists, add all num items.
  
  # if not, 
  pass

def findList(mylist):
  for item in mylist:
    if type(item) == list:
      return True
  return False

print(findList([1,2,3]))
print(findList([1,[2,3]]))
