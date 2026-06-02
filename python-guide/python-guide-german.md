# Lernhilfe Python

## Allgemeine Infos

- Codezeilen werden von oben nach unten ausgeführt.
- Alles, was nach `#` kommt, wird von Python ignoriert. Damit kann man Kommentare für Menschen schreiben.

## Datentypen

Es gibt verschiedene Datentypen in Python:

- **Integer (Ganzzahl)**

    ```python
    5
    ```

- **String (Text)**

    ```python
    "Hello World!"
    "123" # Das ist auch ein String, weil es in "" steht, auch wenn es nur Zahlen sind
    # Mit Strings kann man nicht rechnen.
    ```

- **Float (Kommazahl)**

    ```python
    3.14
    ```

- **Boolean (True oder False)**

    ```python
    True
    False
    ```

## Variablen umwandeln

> [!NOTE]
> Alles, was nach einem `#` kommt, wird von Python ignoriert. Das ist nur eine Notiz für Menschen.

Beispiele:

```python
int(x)   # Umwandeln in Integer (Ganzzahl)
str(x)   # Umwandeln in String (Text)
float(x) # Umwandeln in Float (Kommazahl)

alter = "17" # String (Text)
alter_zahl = int(alter) # Umwandeln in Integer (Ganzzahl)
```

## Variablen zuweisen

Man kann Variablen erstellen und ihnen Werte zuweisen. Man kann sie nennen wie man möchte, aber es ist gut, wenn der Name mit ihrem Inhalt zu tun hat.

```python
a = 5 # Integer (Ganzzahl)
b = 10
name = "Alex" # String (Text), muss "" oder '' haben
```

### Rechnen mit Variablen

Operatoren:

- `+`  Addition
- `-`  Subtraktion
- `*`  Multiplikation
- `/`  Division
- `%`  Modulo (Rest bei Division)

```python
c = a + b # c wird 15 sein, weil 5 + 10 = 15
c = a * b # c wird 50 sein, weil 5 * 10 = 50
a = a + 1 # a wird um 1 erhöht, also a = 6
```

Modulo-Operator gibt den Rest einer Division zurück:

```python
10 % 2 # Gibt 0 zurück. Wenn man 10 durch 2 teilt, ist der Rest 0.
23 % 2 # Gibt 1 zurück. 23 / 2 ergibt 11 mit Rest 1.
```

## Konsole aus-/eingabe

```python
print("Hallo Welt!") # Gibt "Hallo Welt!" in der Konsole aus
```

### User input

```python
print("Wie heisst du?: ")
name = input() # Der User muss in die Konsole etwas eingeben, was dann in der Variable 'name' gespeichert wird
# Abkürzung:
name = input("Wie heisst du?: ")
```

## if-else (Bedingungen)

Mit `if`, `elif` und `else` kann Python Entscheidungen treffen.
Python liest die Bedingungen von oben nach unten und führt nur den ersten passenden Block aus.

Ein Block sind die eingerückten Zeilen unter einer Bedingung. Man muss also Tab drücken, um Python zu zeigen: "Dieser Code gehört zu dieser Bedingung."

`if` = "Wenn diese Bedingung stimmt, mache das hier."<br>
`elif` (optional) = "Sonst, wenn diese andere Bedingung stimmt, mache das hier."<br>
`else` (optional) = "Sonst, wenn keine Bedingung davor gestimmt hat, mache das hier."<br>

> [!NOTE]
> Alles, was nach einem `#` kommt, wird von Python ignoriert. Das ist nur eine Notiz für Menschen und muss nicht abgeschrieben werden.

```python
if a < b: # Wenn a kleiner als b ist
    print("a ist kleiner als b")
elif a == b: # Wenn a gleich b ist
    print("a ist gleich b")
else: # Wenn keine der vorherigen Bedingungen zutrifft
    print("a ist grösser als b")
```

## Schleifen

Schleifen braucht man, wenn Python etwas mehrmals machen soll.
Es gibt 2 wichtige Arten von Schleifen: `for` und `while`.

### for-Schleife

Eine `for`-Schleife geht eine Sammlung Schritt für Schritt durch.
Bei jedem Durchlauf nimmt Python den nächsten Wert aus der Liste und speichert ihn kurz in einer Variable.

```python
fruits = ["Apfel", "Banane", "Kirsche", "Zitrone"]
for fruit in fruits: # fruit ist immer die aktuelle Frucht
    print(fruit) # gibt die aktuelle Frucht aus
```

Python macht hier ungefähr das:

1. `fruit` ist `"Apfel"`, dann wird `"Apfel"` ausgegeben.
2. `fruit` ist `"Banane"`, dann wird `"Banane"` ausgegeben.
3. `fruit` ist `"Kirsche"`, dann wird `"Kirsche"` ausgegeben.
4. `fruit` ist `"Zitrone"`, dann wird `"Zitrone"` ausgegeben.

Output:

```txt
Apfel
Banane
Kirsche
Zitrone
```

Der Name `fruit` ist frei wählbar. Wichtig ist nur, dass du denselben Namen im eingerückten Block wieder benutzt.

Wenn du etwas eine bestimmte Anzahl mal machen willst, kannst du `range()` benutzen:

```python
for i in range(1, 10):
    print("Durchlauf Nummer " + str(i))
```

`range(1, 10)` bedeutet: Starte bei 1 und höre vor 10 auf.
Die 10 ist also nicht mehr dabei.

Output:

```txt
Durchlauf Nummer 1
Durchlauf Nummer 2
Durchlauf Nummer 3
Durchlauf Nummer 4
Durchlauf Nummer 5
Durchlauf Nummer 6
Durchlauf Nummer 7
Durchlauf Nummer 8
Durchlauf Nummer 9
```

### while-Schleife

Eine `while`-Schleife läuft, solange eine Bedingung stimmt.
Python prüft die Bedingung vor jedem Durchlauf neu.

```python
a = 0
b = 5
while a < b: # Solange a kleiner als b ist
    print(a)
    a = a + 1 # a wird grösser, damit die Schleife irgendwann endet
```

Output:

```txt
0
1
2
3
4
```

Wenn `a` den Wert `5` erreicht, stimmt `a < b` nicht mehr. Dann stoppt die Schleife.

Um absichtlich eine Endlosschleife zu machen, kann man `while True:` schreiben.

## Input von dem User bekommen

```python
print("Bitte geben Sie Ihren Namen ein:")
name = input()
```

Wichtig: `input()` gibt immer einen String (Text) zurück (damit kannst du keine Rechnungen machen!). Das Ergebnis kannst du mit `int(...)` in eine Ganzzahl umwandeln:

```python
zahl = int(input("Gib eine Zahl ein: "))
```

> [!TIP]
> Eine Abkürzung: `name = input("Bitte geben Sie Ihren Namen ein:")`

## String Interpolation (Variablen in Strings/Text einfügen)

Es gibt 2 Varianten:

```python
print("Hallo " + name + ", willkommen!") # das '+' verbindet Strings
```

oder

```python
print(f"Hallo {name}, willkommen!") # das 'f' am Anfang muss man hinzufügen, um Variablen mit {} einfügen zu können
```

Wenn die Variable eine Zahl ist, muss man sie zuerst in einen String konvertieren:

```python
age = 17
print("Ich bin " + str(age) + " Jahre alt.")
print(f"Ich bin {age} Jahre alt.") # bei der f-String-Variante wandelt Python die Zahl automatisch in Text um
```

## Arrays / Listen

Anstatt nur eine Variable mit einem Wert, kann man ein Array mit einer Liste von Werten definieren:

```python
fruits = ["Apfel", "Banane", "Kirsche"]
print(fruits[0]) # gibt den ersten Wert des Arrays aus (Man zählt ab 0) (Apfel)
print(fruits[1]) # gibt den zweiten Wert des Arrays aus (Banane)

new_fruit = "Orange"
fruits.append(new_fruit) # Fügt 'Orange' zum Array 'fruits' hinzu
# ["Apfel", "Banane", "Kirsche", "Orange"]
```

String in einen Array (List) umwandeln:

```python
text = "Apfel"
text_array = list(text)
# text_array -> ['A', 'p', 'f', 'e', 'l']
```

Um etwas zum Beispiel 10 mal zu machen:

```python
for i in range(1, 10):
    print(i) # Gibt die Zahlen von 1 bis 9 aus (1, 2, 3, 4, 5, 6, 7, 8, 9)
# 'range(1, 10)' würde einen Array mit den Werten 1 bis 9 erstellen ([1, 2, 3, 4, 5, 6, 7, 8, 9]).
```

Einträge in einem Array zählen:

```python
fruits = ["Apfel", "Banane", "Kirsche"]
anzahl_fruits = len(fruits) # Gibt die Anzahl der Einträge im Array 'fruits' zurück (3 in diesem Fall)
```

## Module

Module kann man importieren, um zusätzliche Funktionen zu nutzen.

Beispiele:

```python
import random
zufall_zahl = random.randint(1, 10) # Gibt eine zufällige Zahl zwischen 1 und 10 zurück

fruits = ["Apfel", "Banane", "Kirsche"]
zufall_frucht = random.choice(fruits) # Gibt eine zufällige Frucht aus dem Array 'fruits' zurück
print(zufall_frucht) # "Kirsche" oder "Banane" oder "Apfel"
```

## Funktionen

Man kann eigene Funktionen erstellen, um wiederholende Logik zu kapseln und den Code übersichtlicher zu machen.

```python
def begruessung(name): # Funktion mit einem Parameter 'name'
    print(f"Hallo {name}, willkommen!") # Gibt eine Begrüssung aus

name = input("Wie heisst du?: ")
begruessung(name) # Ruft die Funktion 'begruessung' mit dem Parameter 'name' auf

def summe(zahl_eins, zahl_zwei): # Funktion mit 2 Parametern 'zahl_eins' und 'zahl_zwei'
    return zahl_eins + zahl_zwei # Gibt die Summe von zahl_eins und zahl_zwei zurück

a = 5
b = 10
resultat = summe(a, b) # a füllt den Parameter 'zahl_eins' und b füllt den Parameter 'zahl_zwei'
print(f"Die Summe von {a} und {b} ist {resultat}.") # Gibt die Summe von a und b aus
```

## Meine Beispiellösungen zu manchen der schwierigen Aufgaben

<https://github.com/Alex7k/learn-python/tree/main/python>
