# Caesar Cipher

ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

text = input("Enter some alphabetical text: ").lower()
key = int(input("Enter an offset key: "))


def cipher(letter, shift):
  for i in range(len(ALPHABET)):
    if letter == ALPHABET[i]:
      return ALPHABET[(i + shift) % len(ALPHABET)]
  return letter  # letter not in alphabet, leave unchanged


shifted_text = ""
for letter in text:
  shifted_text += cipher(letter, key)

print(f"'{text}' caesar-cipher-shifted by {key} turns to '{shifted_text}'")
