def isPalindrome(string):
    # Write your code here.
    # loop to the half of the string
    length = len(string)
    for i in range(int(length / 2)):
        # if the pair is not the same, return False
        if string[i] != string[length - 1 - i]:
            return False
    # after going through the loop successfully, return True
    return True

print(isPalindrome("abc"))
print(isPalindrome("abcba"))