import enchant

characters = "qwertyuiop[]asdfghjkl;'zxcvbnm,./1234567890-=QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?~!@#$%^&*()_+ "

def cypher (text, key):
  """Encrypts text according to a caesar cypher"""
  results = ""
  for letter in text:
    index = characters.find(letter)
    results += characters[(index + key)%len(characters)]
  return results

def decrypt (text, key):
  """Decrypts a Caesar cypher"""
  return cypher (text, -key)

def solve (text):
  """Attempts to decrypt a Caesar Cypher without being given the key"""
  english_words = enchant.Dict("en_US")
  for i in range (len(abcs)):
    real_words=0
    results = ""
    for letter in text:
      results = decrypt(text, i)
      word_array = results.split(" ")
      for word in word_array:
        if word != "" and english_words.check(word):
          real_words+=1
    if real_words / len(word_array) > 0.8:
      return results
  return "Couldn't Break it"

