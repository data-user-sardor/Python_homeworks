from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels
from geometry import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Test math_operations
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))
print("Multiply:", multiply(10, 5))
print("Divide:", divide(10, 5))

# Test string_utils
print("Reverse:", reverse_string("Hello"))
print("Vowel Count:", count_vowels("Hello World"))

# Test geometry.circle
print("Circle Area:", calculate_area(5))
print("Circle Circumference:", calculate_circumference(5))

# Test file_operations
write_file("sample.txt", "This is a test file.")
print("Read File:", read_file("sample.txt"))