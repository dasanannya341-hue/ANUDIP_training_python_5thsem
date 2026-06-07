'''5. Library Book Search 
Problem Statement 
Books available in a library: 
books = [ 
    ("Python Basics", 5), 
    ("Data Science", 0), 
    ("Java Programming", 3), 
    ("Machine Learning", 0) 
] 
Write a program to: 
• Display unavailable books.  
• Find all books with more than 2 copies.  
• Count available books.  
• Stop searching once a requested book is found.'''

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

# Display unavailable books
print("Unavailable Books:")
for book in books:
    if book[1] == 0:
        print(book[0])

# Find books with more than 2 copies
print("\nBooks with more than 2 copies:")
for book in books:
    if book[1] > 2:
        print(book[0])

# Count available books
count = 0
for book in books:
    if book[1] > 0:
        count += 1

print("\nAvailable Books Count:", count)

# Stop searching once a requested book is found
requested = input("\nEnter book name to search: ")

for book in books:
    if book[0] == requested:
        print("Book Found")
        break
else:
    print("Book Not Found")