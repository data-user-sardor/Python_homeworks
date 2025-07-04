# 1 - task Modify String with Underscores. Given a string txt, insert an underscore (_) after every third character. 
# If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. 
# No underscore should be added at the end.
text = "abcabcabcdeabcdefabcdefgll"
# abc_abcab_cdeabcd_efabcdef_g
i = 2
used_chars = ['a', 'e', 'i', 'o', 'u']
while i < len(text) - 1:
    if text[i] not in used_chars:
        text = text[:i+1] + '_' + text[i+1:]
        used_chars.append(text[i])
        i += 4
    else:
        i += 1
print(text)

# 2 - task Integer Squares Exercise. The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input("Type a number "))

for i in range(n):
    print(i ** 2)

# 3 - task Loop-Based Exercises. 
# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1
# Exercise 2: Print the following pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

# Exercise 4: Print multiplication table of a given number

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 75 <= num <= 150:
        print(num)

# Exercise 6: Count the total number of digits in a number

num = int(input("Enter a number: "))
count = 0
while num != 0:
    num //= 10
    count += 1
print("Total digits:", count)

# Exercise 7: Print reverse number pattern

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Exercise 9: Display numbers from -10 to -1 using a for loop

for i in range(-10, 0):
    print(i)

# Exercise 10: Display message “Done” after successful loop execution

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Print all prime numbers within a range

start = 25
end = 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms

n_terms = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n_terms):
    print(a, end='  ')
    a, b = b, a + b

# Exercise 13: Find the factorial of a given number

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"{num}! = {factorial}")

# 4 - task Return Uncommon Elements of Lists.
# Return the elements that are not common between two lists. The order of elements does not matter.
from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    
    result = []

    # Elements only in list1
    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
        else:
            if c1[elem] > c2[elem]:
                result.extend([elem] * (c1[elem] - c2[elem]))

    # Elements only in list2
    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
        else:
            if c2[elem] > c1[elem]:
                result.extend([elem] * (c2[elem] - c1[elem]))
    
    return result
print(uncommon_elements([1, 1, 2], [2, 3, 4]))
print(uncommon_elements([1, 2, 3], [4, 5, 6])) 
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))

