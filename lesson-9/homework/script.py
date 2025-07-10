# Object-Oriented Programming (OOP) Exercises
# 1- task  Circle Class. Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

# 2- task Person Class. Write a Python program to create a Person class. 
# Include attributes like name, country, and date of birth. 
# Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, birthdate):  # birthdate format: YYYY-MM-DD
        self.name = name
        self.country = country
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def age(self):
        today = datetime.today()
        return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

# 3- task Calculator Class. Write a Python program to create a Calculator class. 
# Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Error: Division by zero"

# 4- task Shape and Subclasses. Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# 5- task Binary Search Tree Classю Write a Python program to create a class representing a binary search tree. 
# nclude methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

# 6- task Stack Data Structure. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

# 7- task Linked List Data Structure. Write a Python program to create a class representing a linked list data structure. 
# Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# 8- task Shopping Cart Class. Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_item(self, item, price):
        self.cart[item] = self.cart.get(item, 0) + price

    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]

    def total_price(self):
        return sum(self.cart.values())

# 9- task Stack with Display. Write a Python program to create a class representing a stack data structure. 
# Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def display(self):
        print("Stack:", self.items[::-1])

    def is_empty(self):
        return len(self.items) == 0

# 10- task  Queue Data Structure. Write a Python program to create a class representing a queue data structure. 
# Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

# 11- task Bank Class. Write a Python program to create a class representing a bank. 
# Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, balance=0):
        self.customers[name] = balance

    def deposit(self, name, amount):
        if name in self.customers:
            self.customers[name] += amount

    def withdraw(self, name, amount):
        if name in self.customers and self.customers[name] >= amount:
            self.customers[name] -= amount

    def balance(self, name):
        return self.customers.get(name, "Customer not found")
