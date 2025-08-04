# 1. Age Calculator: Ask the user to enter their birthdate. 
# Calculate and print their age in years, months, and days.
# from datetime import datetime

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += 30  # Approximate days in a month

if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months, and {days} days old.")

# 2. Days Until Next Birthday: Similar to the first exercise, but this time, 
# calculate and print the number of days remaining until the user's next birthday.
# from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
today = datetime.today()
next_birthday = birthdate.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days
print(f"Days until your next birthday: {days_left}")

# 3. Meeting Scheduler: Ask the user to enter the current date and time,
#  as well as the duration of a meeting in hours and minutes. Calculate 
# and print the date and time when the meeting will end.
# from datetime import datetime, timedelta

start_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
hours = int(input("Enter meeting duration hours: "))
minutes = int(input("Enter meeting duration minutes: "))

start_time = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
end_time = start_time + timedelta(hours=hours, minutes=minutes)

print(f"The meeting will end at: {end_time}")

# 4. Timezone Converter: Create a program that allows the user to 
# enter a date and time along with their current timezone, and then 
# convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz

date_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_zone = input("Enter your current timezone (e.g., 'US/Eastern'): ")
to_zone = input("Enter target timezone (e.g., 'Asia/Tokyo'): ")

naive = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
from_tz = pytz.timezone(from_zone)
to_tz = pytz.timezone(to_zone)

localized = from_tz.localize(naive)
converted = localized.astimezone(to_tz)

print(f"Converted date and time: {converted}")


# 5. Countdown Timerr: Implement a countdown timer. 
# Ask the user to input a future date and time, and 
# then continuously print the time remaining until that 
# point in regular intervals (e.g., every second).
from datetime import datetime
import time

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_time = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    diff = future_time - now
    if diff.total_seconds() <= 0:
        print("Time's up!")
        break
    print(f"Time remaining: {diff}", end="\r")
    time.sleep(1)

# 6. Email Validator: Write a program that validates email addresses. 
# Ask the user to input an email address, and check if it follows a valid email format.

import re

email = input("Enter an email address: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# 7. Phone Number Formatter: Create a program that takes a 
# phone number as input and formats it according to a 
# standard format. For example, convert "1234567890" to "(123) 456-7890".

number = input("Enter a 10-digit phone number: ")
formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
print(f"Formatted number: {formatted}")

# 8. Password Strength Checker: Implement a password strength checker. 
# Ask the user to input a password and check if it meets certain criteria 
# (e.g., minimum length, contains at least one uppercase letter, 
# one lowercase letter, and one digit).

import re

password = input("Enter a password: ")

if (len(password) >= 8 and
    re.search(r"[A-Z]", password) and
    re.search(r"[a-z]", password) and
    re.search(r"[0-9]", password)):
    print("Strong password.")
else:
    print("Weak password. Make sure it's at least 8 characters long and contains uppercase, lowercase, and digits.")

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. 
# Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

text = "This is a sample text where the word sample appears multiple times. Sample it again!"
word = input("Enter a word to find: ")

matches = re.findall(rf"\b{word}\b", text, re.IGNORECASE)
print(f"Found '{word}' {len(matches)} times.")

# 10. Date Extractor: Write a program that extracts dates from a given text. 
# Ask the user to input a text, and then identify and print all the dates present in the text.

import re

text = input("Enter text with dates (e.g., 2025-07-16 or 16/07/2025): ")
pattern = r"\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b"

dates = re.findall(pattern, text)
print("Dates found:", dates)
