# 1-task write a Python script that reads the students.jon JSON file and prints details of each student
import json

# Read students.json
with open("D:\Сардор\Личное\Python\Python_homeworks\lesson-14\homework\students.json", "r") as file:
    data = json.load(file)

# Print each student's details
for i, student in enumerate(data["students"], start=1):
    print(f"\nStudent {i}:")
    for key, value in student.items():
        print(f"  {key.capitalize()}: {value}")

# 2-task Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and 
# print relevant information (temperature, humidity, etc.).
import requests

API_KEY = "806d6ad2ec58138c5a7365bd881a1ae6"  # Register at https://openweathermap.org/api to get one
city = "Tashkent"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Condition: {data['weather'][0]['description']}")
else:
    print("Failed to fetch weather data.")
    print(f"Status Code: {response.status_code}")
    print("Response:", response.text)

# 3-task Write a program that allows users to add new books, 
# update existing book information, and delete books from the books.json JSON file.
import json
import os

BOOKS_FILE = r"lesson-14\homework\books.json"

# Load books from file or return empty list
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Display all books
def view_books():
    books = load_books()
    if not books:
        print("\nNo books found.")
        return
    print("\nBooks List:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}")

# Add a new book
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    books = load_books()
    books.append({"title": title, "author": author})
    save_books(books)
    print("Book added successfully.")

# Update an existing book
def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")
    for book in books:
        if book["title"].lower() == title.lower():
            book["title"] = input("New title: ") or book["title"]
            book["author"] = input("New author: ") or book["author"]
            save_books(books)
            print("Book updated successfully.")
            return
    print("Book not found.")

# Delete a book
def delete_book():
    books = load_books()
    title = input("Enter the title of the book to delete: ")
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print("Book deleted successfully.")
            return
    print("Book not found.")

# Main menu loop
def main():
    while True:
        print("\n--- Book Manager ---")
        print("1. View Books")
        print("2. Add Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        choice = input("Choose an option (1–5): ")

        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exiting Book Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# 4-task Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import requests
import random

API_KEY = "ee02e773"  # Replace with your OMDb API key

# Predefined movie titles by genre (since OMDb doesn't allow genre-only search)
genre_movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Gladiator"],
    "Comedy": ["Superbad", "The Grand Budapest Hotel", "Step Brothers"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness"],
    "Sci-Fi": ["Inception", "Interstellar", "The Matrix"],
    "Horror": ["The Conjuring", "A Quiet Place", "Hereditary"],
    "Animation": ["Coco", "Toy Story", "Spirited Away"]
}

# Ask user for genre
genre_input = input("Enter a movie genre (e.g., Action, Comedy, Drama, Sci-Fi): ").capitalize()

# Check if genre is available
if genre_input in genre_movies:
    movie_title = random.choice(genre_movies[genre_input])
    
    # Fetch from OMDb API
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            print(f"\nMovie Recommendation: {data['Title']} ({data['Year']})")
            print(f"Genre: {data['Genre']}")
            print(f"IMDB Rating: {data['imdbRating']}")
            print(f"Plot: {data['Plot']}")
        else:
            print("Movie not found in OMDb.")
    else:
        print("Failed to fetch data from OMDb API.")
else:
    print("Genre not available. Try: " + ", ".join(genre_movies.keys()))
