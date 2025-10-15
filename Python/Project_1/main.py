import string

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

TEXTS = [
'''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

username = input("username: ").lower()
password = input("password: ")

if users.get(username) != password:
    print("Unregistered user, terminating the program..")
    quit()

print("-" * 60)

print(f"Welcome to the app, {username}")
print("We have 3 texts to be analyzed.")
print("-" * 60)

text_number = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
if not text_number.isdigit():
    print("Incorrect input, terminating program..")
    quit()

text_number = int(text_number)
if not 1 <= text_number <= len(TEXTS):
    print("The number is out of range, terminating program..")
    quit()

print("-" * 60)

text = TEXTS[text_number - 1]
words = [word.strip(string.punctuation) for word in text.split()]
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0

word_count = len(words)
for w in words:
    if w.istitle():
        titlecase_count += 1
for w in words:
    if w.isupper():
        uppercase_count += 1
for w in words:
    if w.islower():
        lowercase_count += 1
for w in words:
    if w.isdigit():
        numeric_count += 1

        
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} upppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")