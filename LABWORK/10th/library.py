'''2. Library Book Issue System 
Problem Statement 
A library stores book information in books.txt. 
File Format 
B101,Python Basics,5 
B102,Java Programming,2 
B103,Data Science,0 
B104,DBMS,3 
B105,Machine Learning,1 
B106,Operating Systems,4 
B107,Networking,2 
B108,Cyber Security,6 
B109,Cloud Computing,0 
B110,Web Development,3 
Requirements 
Develop a program to: 
1. Display all books.  
2. Search a book using Book ID.  
3. Issue a book (decrease quantity by 1).  
4. Return a book (increase quantity by 1).  
5. Display unavailable books.  
6. Display books requiring restocking (copies < 2).  
7. Update the file after every issue/return operation'''

# Function to display all books
def display_books():
    file = open("books.txt", "r")
    data = file.readlines()

    print("\nBook Records")
    for line in data:
        print(line.strip())

    file.close()


# Function to search book by ID
def search_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")
    data = file.readlines()

    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0] == book_id:
            print("\nBook Found")
            print("Book ID :", details[0])
            print("Book Name :", details[1])
            print("Quantity :", details[2])
            found = True
            break

    if found == False:
        print("Book not found")

    file.close()


# Function to issue a book
def issue_book():
    book_id = input("Enter Book ID to issue: ")

    file = open("books.txt", "r")
    data = file.readlines()
    file.close()

    new_data = []

    for line in data:
        details = line.strip().split(",")

        if details[0] == book_id:

            if int(details[2]) > 0:
                details[2] = str(int(details[2]) - 1)
                print("Book Issued Successfully")
            else:
                print("Book Not Available")

        new_data.append(",".join(details) + "\n")

    file = open("books.txt", "w")
    file.writelines(new_data)
    file.close()


# Function to return a book
def return_book():
    book_id = input("Enter Book ID to return: ")

    file = open("books.txt", "r")
    data = file.readlines()
    file.close()

    new_data = []

    for line in data:
        details = line.strip().split(",")

        if details[0] == book_id:
            details[2] = str(int(details[2]) + 1)
            print("Book Returned Successfully")

        new_data.append(",".join(details) + "\n")

    file = open("books.txt", "w")
    file.writelines(new_data)
    file.close()


# Function to display unavailable books
def unavailable_books():
    file = open("books.txt", "r")
    data = file.readlines()

    print("\nUnavailable Books")

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) == 0:
            print(details[0], details[1])

    file.close()


# Function to display books requiring restocking
def restocking_books():
    file = open("books.txt", "r")
    data = file.readlines()

    print("\nBooks Requiring Restocking")

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) < 2:
            print(details[0], details[1], details[2])

    file.close()


# Main Program
while True:

    print("\n===== Library Book Issue System =====")
    print("1. Display All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Unavailable Books")
    print("6. Display Books Requiring Restocking")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        search_book()

    elif choice == 3:
        issue_book()

    elif choice == 4:
        return_book()

    elif choice == 5:
        unavailable_books()

    elif choice == 6:
        restocking_books()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")