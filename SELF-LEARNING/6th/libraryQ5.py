'''. Library Book Availability 
Sample Data 
books = { 
    "Python Basics": 5, 
    "Data Structures": 0, 
    "Machine Learning": 3, 
    "Java Programming": 2, 
    "DBMS": 0, 
    "Operating Systems": 6, 
    "Networking": 4, 
    "Cloud Computing": 1, 
    "Cyber Security": 0, 
    "Web Development": 7 
} 
Tasks 
• Display books that are currently unavailable.  
• Count the number of available books.  
• Find the book with the maximum copies.  
• Create a list of books having less than 3 copies.  
• Calculate the total number of books available.  '''


books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display unavailable books
print("Unavailable Books:")
for book in books:
    if books[book] == 0:
        print(book)

# Count available books
count = 0
for book in books:
    if books[book] > 0:
        count += 1

print("\nNumber of Available Books:", count)

# Find book with maximum copies
max_copies = 0
max_book = ""

for book in books:
    if books[book] > max_copies:
        max_copies = books[book]
        max_book = book

print("\nBook with Maximum Copies:")
print(max_book, "(", max_copies, " copies)", sep="")

# Create list of books having less than 3 copies
less_than_3 = []

for book in books:
    if books[book] < 3:
        less_than_3.append(book)

print("\nBooks Having Less Than 3 Copies:")
print(less_than_3)

# Calculate total number of books available
total = 0

for book in books:
    total += books[book]

print("\nTotal Number of Books Available:", total)