### for loop version
# def isPalindrome(string):
#     # loop to the half of the string
#     length = len(string)
#     for i in range(int(length / 2)):
#         # if the pair is not the same, return False
#         if string[i] != string[length - 1 - i] 
#             return False
#     # after going through the loop successfully, return True
#     return True

### pointer version
def isPalindrome(string):
    # set pointers
    left_pointer = 0
    right_pointer = len(string) - 1
    # loop through the pairs to the middle
    while left_pointer < right_pointer:
        # if the pair letters are not the same, return False
        if string[left_pointer] != string[right_pointer]:
            return False
        # in case the pair letters are the same, move pointers one index to the middle 
        left_pointer += 1
        right_pointer -= 1
    # after finishing loop without False case, return True
    return True

print(isPalindrome("abcdcba"))
print(isPalindrome("abcdcbab"))
print(isPalindrome("abccba"))

for i in reversed(range(5)):
    print(i)

for i in range(5):
    print(i)
