

# I know how to update dictionaries 
inventory = {"apples": 10, "bananas": 24, "oranges": 15}

inventory["apples"] = 15
inventory["watermelons"] = 3


for fruit, count in inventory.items():
    print(fruit, count)

print()


# I can use .get to count, but I forgot I can use it for strings. Revisit this. 
user_profile = {"username": "coder99", "email": "code@io.com"}
phone_status = user_profile.get("phone", "No phone on file")

print()


# I can loop through dictionaries and utilize the .items() method.
grades = {"Alice": 92, "Bob": 78, "Charlie": 85, "Diana": 95}

for name, grade in grades.items():
    if grade >= 85:
        print(f"{name}: {grade}")


print()


# This is called grouping. I did not get it right, revisit this because I needed help 
employees = {"Alice": "HR", "Bob": "IT", "Charlie": "HR", "Diana": "Sales"}

departments = {}

for name, dept in employees.items():
    if dept not in departments:
        departments[dept] = []
        
    departments[dept].append(name)

print(departments)

print()


# I understand how to delete keys and values.
cart = {"Laptop": 1200, "Mouse": 25, "Keyboard": 45, "Monitor": 300}

del cart["Mouse"]
print(cart)


# Revisting...

user_profile = {"username": "travel_bug", "status": "Active"}

user_bio = user_profile.get("bio", "This user hasn't written a bio yet.")

print()

books = {
    "Dune": "Sci-Fi",
    "Dracula": "Horror",
    "Foundation": "Sci-Fi",
    "The Hobbit": "Fantasy",
    "Frankenstein": "Horror"
}

genres = {}

for title, genre, in books.items():
    if genre not in genres:
        genres[genre] = [] # initialize a new list
        
        genres[genre].append(title)

print(books)