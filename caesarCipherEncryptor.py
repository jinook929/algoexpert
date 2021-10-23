def caesarCipherEncryptor(string, key):
    encrypted = []
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    for ch in string:
        index = alphabet.index(ch)
        encryptedindex = index + key
        if encryptedindex < 26:
            encrypted.append(alphabet[encryptedindex])
        else:
            encrypted.append(alphabet[encryptedindex - 26]) 
    return "".join(encrypted)

print(caesarCipherEncryptor("xyz", 2))