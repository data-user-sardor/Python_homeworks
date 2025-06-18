import math
# 1. Square: Perimeter and Area
side = float(input("Enter the side of the square: "))
square_perimeter = 4 * side
square_area = side ** 2
print(f"Square - Perimeter: {square_perimeter}, Area: {square_area}")

# 2. Circle: Circumference
diameter = float(input("\nEnter the diameter of the circle: "))
circle_circumference = math.pi * diameter
print(f"Circle - Circumference (Length): {circle_circumference}")

# 3. Mean of two numbers
a = float(input("\nEnter first number (a): "))
b = float(input("Enter second number (b): "))
mean = (a + b) / 2
print(f"Mean of {a} and {b}: {mean}")

# 4. Sum, Product, Squares
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(f"Sum: {sum_ab}")
print(f"Product: {product_ab}")
print(f"Square of {a}: {square_a}")
print(f"Square of {b}: {square_b}")
