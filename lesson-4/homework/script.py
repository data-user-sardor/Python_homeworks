#1-task. Write a Python script to sort (ascending and descending) a dictionary by value
my_dict = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(my_dict.items(), key=lambda x: x[1])))  # Ascending
print(dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True)))  # Descending

#2-task. Write a Python script to add a key to a dictionary
my_dict = {0: 10, 1: 20}
my_dict[2] = 30 # Add a new key-value pair
print(my_dict)

#3-task. Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {**dic1, **dic2, **dic3}  # Concatenate dictionaries
print(result)

#4-task. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
squares = {x: x * x for x in range(1, n + 1)}
print(squares)

#5-task. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
squares = {x: x * x for x in range(1, 16)}
print(squares)

#6-task. Create a Set
my_set = {1, 2, 3}
print("Set:", my_set)

#7-task. Iterate Over a Set
my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item) # Iterate through the set

#8-task. Add Member(s) to a Set
my_set = {1, 2, 3}
my_set.add(4) # Add a single item
my_set.update([5, 6]) # Add multiple items
print("Updated set:", my_set)

#9-task. Remove Item(s) from a Set
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)  # Raises KeyError if item not found
my_set.discard(4) # Does not raise error if item not found
print("After removal:", my_set)

#10-task. Remove an Item if Present in the Set
my_set = {1, 2, 3, 4}
item_to_remove = 3
if item_to_remove in my_set:
    my_set.remove(item_to_remove)   # Remove an item only if it's present
print("Updated set:", my_set)
