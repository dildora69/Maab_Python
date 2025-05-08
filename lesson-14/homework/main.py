import json
import requests

# 1. Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.

# with open('students.json') as f:
#     data = json.load(f)
#     for i in data['students']:
#         print(i)

# 2. Task: Weather API

# parameters = {
#     'appid': 'f1ec03a66500e9355b99280d097ac492',
#     'units': 'metric',
#     'lang': 'en'
# }
#
# while True:
#     city_name = input('Enter the name of a City: ')
#     parameters['q'] = city_name
#
#     try:
#         weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
#         name = weather['name']
#         temp = weather['main']['temp']
#         description = weather['weather'][0]['description']
#         timezone = weather['timezone']
#
#         print(f''' In the City {name} now {description}
# Temperature: {temp} °C
# TimeZone: {timezone}''')
#
#     except Exception as e:
#         print('You Entered wrong City Name.')\


# 3. Task: JSON Modification


filename = "books.json"

def load_books():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(filename, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    book = {
        "id": input("Book ID: "),
        "title": input("Title: "),
        "author": input("Author: "),
        "year": input("Year: ")
    }
    books.append(book)
    save_books(books)
    print("Book added.\n")

def update_book():
    books = load_books()
    book_id = input("Enter ID of book to update: ")
    for book in books:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            book["year"] = input("New year: ")
            save_books(books)
            print("Book updated.\n")
            return
    print("Book not found.\n")

def delete_book():
    books = load_books()
    book_id = input("Enter ID of book to delete: ")
    books = [b for b in books if b["id"] != book_id]
    save_books(books)
    print("Book deleted if it existed.\n")

def main():
    while True:
        print("1. Add\n2. Update\n3. Delete\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice.\n")

main()

