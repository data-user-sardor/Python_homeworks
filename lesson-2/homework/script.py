# 1. Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
current_year = 2025
age = current_year - birth_year
print(f"{name}, you are {age} years old.\n")

# 2. Extract Car Names 
txt = 'LMaasleitbtui'
even_indexed = ''.join([txt[i] for i in range(0, len(txt), 2)])
odd_indexed = ''.join([txt[i] for i in range(1, len(txt), 2)])
print("Even-indexed chars:", even_indexed)
print("Odd-indexed chars:", odd_indexed)

# 3. Extract Car Names 
txt = 'MDaatmiazs'
even_indexed = ''.join([txt[i] for i in range(0, len(txt), 2)])  # индексы: 0, 2, 4,...
odd_indexed = ''.join([txt[i] for i in range(1, len(txt), 2)])   # индексы: 1, 3, 5,...
print("Even-indexed chars:", even_indexed)
print("Odd-indexed chars:", odd_indexed)

# 4. Extract Residence Area
txt = "I'am John. I am from London"
start = txt.find("from") + 5
residence = txt[start:]
print("Residence area:", residence)

# 5. Reverse String
user_input = input("Enter a string: ")
reversed_string = user_input[::-1]
print("Reversed string:", reversed_string)

# 6. Count Vowels
text = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)

# 7. Find Maximum Value
nums = input("Enter numbers separated by spaces: ")
num_list = list(map(float, nums.split()))
maximum = max(num_list)
print("Maximum value:", maximum)

# 8.Check Palindrome
word = input("Enter a word: ")
word_clean = word.lower()
if word_clean == word_clean[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
 
 # 9. Extract Email Domain
email = input("Enter your email address: ")
domain = email.split('@')[-1]
print("Email domain:", domain)

# 10. Generate Random Password
import random
import string
length = 12
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print("Generated password:", password)
