# Python Exception Handling: Exercises, Solutions, and Practice
# Exception Handling Exercises
# 1 exercise Handle ZeroDivisionError

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 2 exercise  Raise ValueError if input is not a valid integer

try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: That is not a valid integer.")


# 3 exercise Handle FileNotFoundError

try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found.")


# 4 exercise Raise TypeError if inputs are not numerical

try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Sum:", x + y)
except ValueError:
    raise TypeError("Error: Both inputs must be numbers.")


# 5 exercise Handle PermissionError when opening a file

try:
    with open("/root/protected_file.txt", "r") as f:
        data = f.read()
except PermissionError:
    print("Error: Permission denied.")


# 6 exercise Handle IndexError in list operations

my_list = [10, 20, 30]
try:
    index = int(input("Enter index to access (0-2): "))
    print("Value:", my_list[index])
except IndexError:
    print("Error: Index out of range.")


# 7 exercise Handle KeyboardInterrupt during input

try:
    num = input("Enter a number (Ctrl+C to cancel): ")
    print("You entered:", num)
except KeyboardInterrupt:
    print("\nInput cancelled by user.")


# 8 exercise Handle ArithmeticError during division

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter divisor: "))
    result = a / b
    print("Result:", result)
except ArithmeticError as e:
    print("Arithmetic error occurred:", e)


# 9 exercise Handle UnicodeDecodeError when reading a file

try:
    with open("some_file.txt", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    print("Error: Could not decode file due to encoding issue.")


# 10 exercise Handle AttributeError in list operations

my_list = [1, 2, 3]
try:
    my_list.append(4)
    my_list.upper()  # Invalid method for list
except AttributeError as e:
    print("Attribute error:", e)


# Python File Input Output: Exercises, Practice, Solution
# File Input/Output Exercises

# 1 exercise Read entire text file

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# 2 exercise Read first n lines of a file

n = 3
with open("example.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")

# 3 exercise Append text to a file and display it

with open("example.txt", "a") as file:
    file.write("\nNew line added.")

with open("example.txt", "r") as file:
    print(file.read())

# 4 exercise Read last n lines of a file

n = 3
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(''.join(lines[-n:]))

# 5 exercise Read a file line by line into a list

with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)

# 6 exercise Read file line by line into a variable

with open("example.txt", "r") as file:
    content = ""
    for line in file:
        content += line
print(content)

# 7 exercise Read file line by line into an array

with open("example.txt", "r") as file:
    array = [line.strip() for line in file]
print(array)

# 8 exercise Find the longest words in a file

with open("example.txt", "r") as file:
    words = file.read().split()
    max_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_len]
print("Longest word(s):", longest_words)

# 9 exercise Count the number of lines in a text file

with open("example.txt", "r") as file:
    count = sum(1 for _ in file)
print("Number of lines:", count)

# 10 exercise Count the frequency of words in a file

from collections import Counter

with open("example.txt", "r") as file:
    words = file.read().replace(",", " ").split()
    freq = Counter(words)
print(freq)

# 11 exercise Get the file size of a plain file

import os

file_size = os.path.getsize("example.txt")
print("File size (bytes):", file_size)

# 12 exercise Write a list to a file

lines = ["Apple", "Banana", "Cherry"]
with open("fruits.txt", "w") as file:
    for item in lines:
        file.write(item + "\n")

# 13 exercise Copy contents of a file to another

with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
    dst.write(src.read())

# 14 exercise Combine lines from two files line-by-line

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15 exercise Read a random line from a file

import random

with open("example.txt", "r") as file:
    lines = file.readlines()
    print("Random line:", random.choice(lines).strip())

# 16 exercise Check if a file is closed

file = open("example.txt", "r")
print("File closed?", file.closed)
file.close()
print("File closed?", file.closed)

# 17 exercise Remove newline characters from a file

with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)

# 18 exercise Count number of words in a text file

with open("example.txt", "r") as file:
    text = file.read().replace(",", " ")
    words = text.split()
print("Word count:", len(words))

# 19 exercise Extract characters from files into a list

import glob

char_list = []
for filename in glob.glob("*.txt"):
    with open(filename, "r") as file:
        char_list.extend(list(file.read()))
print(char_list)

# 20 exercise Generate 26 files named A.txt to Z.txt

import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as file:
        file.write(f"This is {letter}.txt\n")

# 21 exercise  Create a file with alphabet letters, N per line

import string

n = 5
letters = string.ascii_lowercase
with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        file.write(' '.join(letters[i:i+n]) + "\n")
