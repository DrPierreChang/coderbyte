import string


def LongestWord(sen):
  longest_word = None
  longest_word_len = 0

  for word in (sen.translate(str.maketrans('','', string.punctuation))\
  .split()):
    if len(word) > longest_word_len:
      longest_word = word
      longest_word_len = len(word)

  return longest_word

# keep this function call here 
print(LongestWord(input()))
