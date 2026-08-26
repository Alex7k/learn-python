# Python script ideas

This file contains Python scripting ideas.

If you are stuck, there is usually a finished example in the `python/` folder to look at.

Use the [python guide](./python-guide) to learn about concepts used in these exercises

## Level 1 (Start here)

- 18+ checker by age
  - Provide an age
  - Print "You are 18 or above" or "You are underage"
  - <details><summary>Hint</summary>Use <code>if</code>, <code>&lt;</code> or <code>&gt;</code> and <code>else</code></details>

- Calculator
  - Sum (+) 2 user-defined numbers
  - <details><summary>Hint</summary>Use <code>int(input())</code> to get two numbers from the user</details>
  - Extra: Let the user decide between operands `+`, `-`, `*`, or `/`
    - <details><summary>Hint</summary>Use <code>input()</code> so the user can choose an operand, then do something like:<br><code>if operand == "+":</code><br><code>    result = first_num + second_num</code></details>

- [Palindrome](https://en.wikipedia.org/wiki/Palindrome) checker
  - Definition: A word that stays the same when read backwards. E.g. 'racecar' or 'madam'

## Level 2

- User math trainer
  - Generate random math problem (`+`, `-` or `*`)
  - User calculates and enters his answer
  - Tell the user whether his answer is correct
  - Tip: Avoid `/` for now

- Random password generator
  - Generate a string of random characters. E.g. `wgH^@Q60bIr1YGw3`
  - Use `import random`
  - <details><summary>Hint</summary>Define a list of characters: <code>characters = list("abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+")</code> and use <code>random.choice(characters)</code> to get a random character</details>

- Random number guessing game
  - "Guess a number:", "Too high!", "Too low!", "You win!"
  - <details><summary>Hint</summary>Use <code>&lt;</code> and <code>&gt;</code></details>

## Level 3

- Prime number checker
  - Provide any number
  - Rule for Prime Numbers: A prime number can only be divided by 1 and itself
  - <details><summary>Hint 1</summary>Use the modulo operator <code>%</code> (<code>x % y</code> equals <code>0</code> if <strong>x</strong> is divisible by <strong>y</strong>, meaning there is no remainder)</details>
  - <details><summary>Hint 2</summary>Assume it's a prime, then try to <em>prove</em> that it's not</details>

- [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
  - Provide a starting number
  - Rules
    - If even, divide by 2
    - If odd, multiply by 3 and add 1
  - Stop when you reach 1

- Fibonacci sequence
  - Starting numbers are: 0, 1
  - 0 1 1 2 3 5 8 13 21 34 55 (Next number is the sum of the last two)
  - <details><summary>Hint</summary>Use a "temp" variable</details>
  <!-- - Extra: There is also a more intuitive way using arrays -->

## Level 4

- [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) encoder
  - Set an alphabet list: `alphabet = list("abcdefghijklmnopqrstuvwxyz")`
  - Provide a starting word
  - Provide a number
  - Rule of Caesar Cipher: All letters in the word are "shifted" in the alphabet based on the number. `abc` with number `1` becomes `bcd`.
  - Extra: Make sure if you shift e.g. `z` by `2`, it wraps back to the start and returns `b`.
    - <details><summary>Hint</summary>Use the modulo operator <code>%</code> with the alphabet length <code>len(alphabet)</code></details>

- [Anagram](https://en.wikipedia.org/wiki/Anagram) Finder
  - Make a wordlist with a bunch of words (E.g.: "listen", "silent", "dormitory", "dirty room", "debit card", "bad credit")
  - Tip: Do Palindrome checker first!
  - Definition: "a word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp."
  - <details><summary>Hint</summary>Use <code>sorted()</code>. Two words are anagrams if <code>sorted(word_one)</code> equals <code>sorted(word_two)</code>.</details>

## Level 5

- [Hangman](https://en.wikipedia.org/wiki/Hangman_(game))
  - A random word is chosen. The user doesn't know the word. The user guesses one letter at a time.
  - Reveal all occurrences of a letter after it has been guessed.<br>
    Let's say the word is banana: `______` -> user guesses `a` -> `_a_a_a` and so on.
  - The user wins if all letters have been revealed.
    - <details><summary>Hint</summary>Check if there are no `_`s (empty fields) left</details>
  - Extra: Give the user 5 "hearts" and make him lose if he has no hearts left

- [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe)
  - Create a playing board (array with 9 slots)
  - Let user pick a position to play
  - Alternate between player `X` and player `O`
  - Display the board after every move
  - Win condition: 3 in a row (horizontally, vertically, on the diagonal)

## Level 6 (Advanced)

- [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

- Minesweeper

- Sudoku Game

- Maze Generator and Solver
