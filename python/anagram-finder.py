dict = [
    "apple",
    "banana",
    "cherry",
    "date",
    "earth",
    "heart",
    "rathe",
    "fried",
    "fired",
    "listen",
    "silent",
    "dormitory",
    "dirty room",
    "debit card",
    "bad credit",
]

input_word = "fried"

anagrams = []
for word in dict:
    normalized_input = input_word.replace(" ", "")
    normalized_word = word.replace(" ", "")
    if len(normalized_input) == len(normalized_word) and input_word != word:
        if sorted(list(normalized_input)) == sorted(list(normalized_word)):
            anagrams.append(word)

print(f"Anagrams to '{input_word}':")
print(anagrams)
