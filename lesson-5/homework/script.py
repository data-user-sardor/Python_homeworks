# - 1 task
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage
if __name__ == "__main__":
    test_years = [1600, 1700, 1800, 1900, 2000, 2020, 2021, 2024]
    for year in test_years:
        print(f"{year}: {'Leap Year' if is_leap(year) else 'Not a Leap Year'}")


# - 2 task Given an integer, n, perform the following conditional actions:
#     If n is odd, print Weird
#     If n is even and in the inclusive range of 2 to 5, print Not Weird
#     If n is even and in the inclusive range of 6 to 20, print Weird
#     If n is even and greater than 20, print Not Weird
# Input Format
# A single line containing a positive integer, n.
# Constraints
#     1 <= n <= 100
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

n = int(input("Enter a number: ").strip())
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

# - 3 task Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop
# Using if-else
a = 3
b = 12
start = a if a % 2 == 0 else a + 1 
even_numbers = list(range(start, b + 1, 2)) if start <= b else []
print(even_numbers)

# Without if or else
a = 3
b = 12
start = a + (a % 2)
even_numbers = list(range(start, b + 1, 2)) * (start <= b)
print(even_numbers)

