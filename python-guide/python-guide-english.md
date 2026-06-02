# Python Learning Aid (MACHINE TRANSLATED)

## General Information

- Code lines are executed from top to bottom.
- Everything after `#` is ignored by Python. You can use this to write comments for humans.

## Data Types

There are different data types in Python:

- **Integer (Whole number)**

    ```python
    5
    ```

- **String (Text)**

    ```python
    "Hello World!"
    "123" # This is also a string because it is in "", even if it only contains numbers
    # You cannot do math with strings.
    ```

- **Float (Decimal number)**

    ```python
    3.14
    ```

- **Boolean (True or False)**

    ```python
    True
    False
    ```

## Converting Variables

> [!NOTE]
> Everything after a `#` is ignored by Python. It is only a note for humans.

Examples:

```python
int(x)   # Convert to integer (whole number)
str(x)   # Convert to string (text)
float(x) # Convert to float (decimal number)

age = "17" # String (text)
age_number = int(age) # Convert to integer (whole number)
```

## Assigning Variables

You can create variables and assign values to them. You can name them as you like, but it's good if the name relates to their content.

```python
a = 5 # Integer (whole number)
b = 10
name = "Alex" # String (text), must have "" or ''
```

### Calculating with Variables

Operators:

- `+`  Addition
- `-`  Subtraction
- `*`  Multiplication
- `/`  Division
- `%`  Modulo (remainder of division)

```python
c = a + b # c will be 15 because 5 + 10 = 15
c = a * b # c will be 50 because 5 * 10 = 50
a = a + 1 # a is increased by 1, so a = 6
```

Modulo operator returns the remainder of a division:

```python
10 % 2 # Returns 0. When you divide 10 by 2, the remainder is 0.
23 % 2 # Returns 1. 23 / 2 is 11 with remainder 1.
```

## Console Output/Input

```python
print("Hello World!") # Prints "Hello World!" to the console
```

### User input

```python
print("What is your name?: ")
name = input() # The user must enter something in the console, which is then stored in the variable 'name'
# Shortcut:
name = input("What is your name?: ")
```

## if-else (Conditions)

With `if`, `elif`, and `else`, Python can make decisions.
Python reads the conditions from top to bottom and only runs the first matching block.

A block is the indented lines below a condition. So you press Tab to show Python: "This code belongs to this condition."

`if` = "If this condition is true, do this."<br>
`elif` (optional) = "Otherwise, if this other condition is true, do this."<br>
`else` (optional) = "Otherwise, if none of the conditions above were true, do this."<br>

> [!NOTE]
> Everything after a `#` is ignored by Python. It is only a note for humans and does not need to be copied.

```python
if a < b: # If a is less than b
    print("a is less than b")
elif a == b: # If a is equal to b
    print("a is equal to b")
else: # If none of the previous conditions apply
    print("a is greater than b")
```

## Loops

You need loops when Python should do something multiple times.
There are 2 important types of loops: `for` and `while`.

### for loop

A `for` loop goes through a collection step by step.
On each loop run, Python takes the next value from the list and stores it temporarily in a variable.

```python
fruits = ["Apple", "Banana", "Cherry", "Lemon"]
for fruit in fruits: # fruit is always the current fruit
    print(fruit) # prints the current fruit
```

Python roughly does this:

1. `fruit` is `"Apple"`, then `"Apple"` is printed.
2. `fruit` is `"Banana"`, then `"Banana"` is printed.
3. `fruit` is `"Cherry"`, then `"Cherry"` is printed.
4. `fruit` is `"Lemon"`, then `"Lemon"` is printed.

Output:

```txt
Apple
Banana
Cherry
Lemon
```

The name `fruit` can be chosen freely. The important part is that you use the same name again in the indented block.

If you want to do something a specific number of times, you can use `range()`:

```python
for i in range(1, 10):
    print("Loop run number " + str(i))
```

`range(1, 10)` means: Start at 1 and stop before 10.
So 10 is not included.

Output:

```txt
Loop run number 1
Loop run number 2
Loop run number 3
Loop run number 4
Loop run number 5
Loop run number 6
Loop run number 7
Loop run number 8
Loop run number 9
```

### while loop

A `while` loop runs as long as a condition is true.
Python checks the condition again before every loop run.

```python
a = 0
b = 5
while a < b: # As long as a is less than b
    print(a)
    a = a + 1 # a gets bigger so the loop eventually ends
```

Output:

```txt
0
1
2
3
4
```

When `a` reaches the value `5`, `a < b` is no longer true. Then the loop stops.

To make an infinite loop, you can write `while True:`.

## Getting Input from the User

```python
print("Please enter your name:")
name = input()
```

Important: `input()` always returns a string (text), so you cannot do calculations with it directly. You can convert the result to a whole number with `int(...)`:

```python
number = int(input("Enter a number: "))
```

> [!TIP]
> Shortcut: `name = input("Please enter your name:")`

## String Interpolation (Insert variables into strings/text)

There are 2 variants:

```python
print("Hello " + name + ", welcome!") # '+' joins strings
```

or

```python
print(f"Hello {name}, welcome!") # You must add 'f' at the beginning to insert variables with {}
```

If the variable is a number, you must first convert it to a string:

```python
age = 17
print("I am " + str(age) + " years old.")
print(f"I am {age} years old.") # with the f-string variant, Python automatically converts the number to text
```

## Arrays / Lists

Instead of just one variable with one value, you can define an array with a list of values:

```python
fruits = ["Apple", "Banana", "Cherry"]
print(fruits[0]) # prints the first value of the array (Counting starts at 0) (Apple)
print(fruits[1]) # prints the second value of the array (Banana)

new_fruit = "Orange"
fruits.append(new_fruit) # Adds 'Orange' to the array 'fruits'
# ["Apple", "Banana", "Cherry", "Orange"]
```

Convert a string to an array (list):

```python
text = "Apple"
text_array = list(text)
# text_array -> ['A', 'p', 'p', 'l', 'e']
```

To do something, for example, 10 times:

```python
for i in range(1, 10):
    print(i) # Prints the numbers from 1 to 9 (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 'range(1, 10)' would create an array with the values 1 to 9 ([1, 2, 3, 4, 5, 6, 7, 8, 9]).
```

Count entries in an array:

```python
fruits = ["Apple", "Banana", "Cherry"]
number_of_fruits = len(fruits) # Returns the number of entries in the array 'fruits' (3 in this case)
```

## Modules

You can import modules to use additional functions.

Examples:

```python
import random
random_number = random.randint(1, 10) # Returns a random number between 1 and 10

fruits = ["Apple", "Banana", "Cherry"]
random_fruit = random.choice(fruits) # Returns a random fruit from the array 'fruits'
print(random_fruit) # "Cherry" or "Banana" or "Apple"
```

## Functions

You can create your own functions to encapsulate repeating logic and make the code clearer.

```python
def greeting(name): # Function with one parameter 'name'
    print(f"Hello {name}, welcome!") # Prints a greeting

name = input("What is your name?: ")
greeting(name) # Calls the function 'greeting' with the parameter 'name'

def sum_numbers(number_one, number_two): # Function with 2 parameters 'number_one' and 'number_two'
    return number_one + number_two # Returns the sum of number_one and number_two

a = 5
b = 10
result = sum_numbers(a, b) # a fills the parameter 'number_one' and b fills the parameter 'number_two'
print(f"The sum of {a} and {b} is {result}.") # Prints the sum of a and b
```

## My example solutions to some of the more difficult tasks

<https://github.com/Alex7k/learn-python/tree/main/python>
