# def runLengthEncoding(string):
#   # Write your code here.
#   length = len(string)
#   result = ""
#   current = string[0]
#   charcounts = {}
#   # loop through the string
#   for i in range(length):
#     # count number of consecutive same char and store it in dict
#     charcounts[string[i]] = charcounts.get(string[i], 0) + 1
#     # if char is different from the previous one,
#     if i != 0 and string[i] != current:
#       # add the count of the prev char with the prev char to result
#       result += str(charcounts[current])
#       result += current
#       charcounts[current] = 0
#       current = string[i]
#     # if the count of char is greater than 9, 
#     if charcounts[string[i]] > 9:
#       # add 9 with the prev char to result
#       result += "9"
#       result += string[i]
#       charcounts[current] = 1
#     # when last char, add current char with its count before
#     if i == length - 1:
#       result += str(charcounts[string[i]])
#       result += string[i]
#   return result


def runLengthEncoding(string):
  length = len(string)
  result = []
  current = string[0]
  charcounts = {}
  for i in range(length):
    charcounts[string[i]] = charcounts.get(string[i], 0) + 1
    if i != 0 and string[i] != current:
      result.append(f"{str(charcounts[current])}{current}")
      charcounts[current] = 0
      current = string[i]
    if charcounts[string[i]] > 9:
      result.append(f"9{current}")
      charcounts[current] = 1
  result.append(f"{str(charcounts[string[i]])}{string[i]}")
  return "".join(result)

print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDDAAABBC"))