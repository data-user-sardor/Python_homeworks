#1-task. Create a list containing five different fruits and print the third fruit
fruits = ["apple", "banana", "cherry", "orange", "grape"]
print(fruits[2])

#2-task. Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

#3-task. Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]
extracted = [first, middle, last]
print(extracted)

#4-task. Create a list of your five favorite movies and convert it into a tuple.
favorite_movies = ["Avatar", "The Matrix", "Interstellar", "Titanic", "Forrest Gump"]
movies_tuple = tuple(favorite_movies)
print(movies_tuple)

#5-task. Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["London", "New York", "Tokyo", "Paris", "Sydney"]
if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

#6-task. Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3, 4, 5]
duplicated_list = numbers * 2
print(duplicated_list)

#7-task. Given a list of numbers, swap the first and last elements.
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

#8-task. Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_tuple = numbers[3:7]
print(slice_tuple)

#9-task. Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
blue_count = colors.count("blue")
print("Blue appears", blue_count, "times.")

#10-task. Given a tuple of animals, find the index of "lion".
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print("The index of 'lion' is:", lion_index)

#11-task. Create two tuples of numbers and merge them into a single tuple.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

#12-task. Given a list and a tuple, find and print their lengths.
my_list = [10, 20, 30, 40, 50]
my_tuple = ("apple", "banana", "cherry")
list_length = len(my_list)
tuple_length = len(my_tuple)
print("Length of the list:", list_length)
print("Length of the tuple:", tuple_length)

#13-task. Create a tuple of five numbers and convert it into a list.
numbers_tuple = (10, 20, 30, 40, 50)
numbers_list = list(numbers_tuple)
print(numbers_list)

#14-task. Given a tuple of numbers, find and print the maximum and minimum values. 
numbers = (15, 8, 22, 4, 19, 31, 7)
maximum = max(numbers)
minimum = min(numbers)
print("Maximum value:", maximum)
print("Minimum value:", minimum)

#15-task. Create a tuple of words and print it in reverse order.
words = ("apple", "banana", "cherry", "date", "blueberry")
reversed_words = words[::-1]
print(reversed_words)
