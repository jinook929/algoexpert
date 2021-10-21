def firstNonRepeatingCharacter(string):
    # create a dict of chars with the number of their occurances 
    charcount = {}
    for ch in string:
        charcount[ch] = charcount.get(ch, 0) + 1
        # if ch not in charcount:
        #     charcount[ch] = 1
        # else:
        #     charcount[ch] += 1
    # loop through the string and find the index of char whose index is 1
    for i in range(len(string)):
        if charcount[string[i]] == 1:
            return i
    return -1

print(firstNonRepeatingCharacter("abcde"))
print(firstNonRepeatingCharacter("abcbadce"))
print(firstNonRepeatingCharacter("abcdcaf"))