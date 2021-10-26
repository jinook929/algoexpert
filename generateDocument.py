def generateDocument(characters, document):
  chars = {}
  docs = {}
  docset = set()

  for ch in characters:
    chars[ch] = chars.get(ch, 0) + 1

  for ch in document:
    docs[ch] = docs.get(ch, 0) + 1
    docset.add(ch)

  for ch in docset:
    if ch not in chars or chars[ch] < docs[ch]:
      return False

  return True

characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument(characters, document))

characters = "abcabc" 
document = "aabbccc"
print(generateDocument(characters, document))

characters = "a" 
document = "A"
print(generateDocument(characters, document))