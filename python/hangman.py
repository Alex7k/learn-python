import random

wordlist = [ "apple", "banana", "burger", "equilibrium", "operator", "keyboard", "paragraph", "obituary", "technology", "optimal" ]
word = list(random.choice(wordlist)) # e.g. banana
temp = list("_"*len(word)) # e.g. ______

guessedletters = []

while True:
  print(" ".join(temp))
  print(f"Guessed letters: {" ".join(guessedletters)}")
  if temp == list(word):
    print(f"You won with {len(guessedletters)} tries!")
    exit()
  userinput = input("Guess a letter: ")
  if len(userinput) != 1:
    print("Only one letter please!")
    continue
  if userinput in guessedletters:
    print("You've already guessed that letter!")
    continue
  else:
    guessedletters.append(userinput)
    for i in range(len(word)):
      if userinput == word[i]:
        temp[i] = word[i]