import random
import sys

WORDLIST = [
    "apple",
    "banana",
    "burger",
    "equilibrium",
    "operator",
    "keyboard",
    "paragraph",
    "obituary",
    "technology",
    "optimal",
]
HEARTS = 5

word = list(random.choice(WORDLIST))  # e.g. banana
temp = list("_" * len(word))  # e.g. ______

guessedletters = []

while True:
    print(" ".join(temp))  # display status (e.g. "b _ n _ n _")
    print(f"Guessed letters: {', '.join(guessedletters)}")
    if temp == list(word):
        print(f"You won with {len(guessedletters)} tries!")
        sys.exit()
    userinput = input("Guess a letter: ").lower()
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
