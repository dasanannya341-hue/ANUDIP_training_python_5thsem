'''3. Smart Library Management System 
Problem Statement 
Create a digital library management system. 
Example Structure 
library = { 
    "B101": { 
        "title": "Python Basics", 
        "author": "ABC", 
        "copies": 5 
    } 
} 
Maintain records of at least 30 books. 
Requirements 
1. Add a book.  
2. Remove a book.  
3. Search a book by ID.  
4. Search by title.  
5. Update available copies.  
6. Issue a book.  
7. Return a book.  
8. Display books with fewer than 3 copies.  
9. Display books that are unavailable.  
10. Find the most available book.  
11. Generate a restocking report.  
12. Create a separate dictionary of books requiring immediate purchase.  
Challenge 
Generate a complete library summary report.'''

# Smart Library Management System

library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Structures", "author": "XYZ", "copies": 2},
    "B103": {"title": "Machine Learning", "author": "PQR", "copies": 0},
    "B104": {"title": "DBMS", "author": "MNO", "copies": 4},
    "B105": {"title": "Operating Systems", "author": "RST", "copies": 1}
}

while True:

    print("\n===== SMART LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display All Books")
    print("2. Add Book")
    print("3. Remove Book")
    print("4. Search Book by ID")
    print("5. Search Book by Title")
    print("6. Update Copies")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Books with Less Than 3 Copies")
    print("10. Unavailable Books")
    print("11. Most Available Book")
    print("12. Restocking Report")
    print("13. Immediate Purchase Report")
    print("14. Library Summary Report")
    print("15. Exit")

    choice = int(input("Enter Choice : "))

    # --------------------------------------------------
    # Display all books

    if choice == 1:

        print("\nLibrary Records")

        dict_items = list(library.items())

        for item in dict_items:
            print(item[0], ":", item[1])

    # --------------------------------------------------
    # Add book

    elif choice == 2:

        book_id = input("Enter Book ID : ")
        title = input("Enter Title : ")
        author = input("Enter Author : ")
        copies = int(input("Enter Copies : "))

        library[book_id] = {
            "title": title,
            "author": author,
            "copies": copies
        }

        print("Book Added Successfully")

    # --------------------------------------------------
    # Remove book

    elif choice == 3:

        book_id = input("Enter Book ID : ")

        if book_id in library:
            del library[book_id]
            print("Book Removed")
        else:
            print("Book Not Found")

    # --------------------------------------------------
    # Search by ID

    elif choice == 4:

        book_id = input("Enter Book ID : ")

        if book_id in library:
            print(library[book_id])
        else:
            print("Book Not Found")

    # --------------------------------------------------
    # Search by title

    elif choice == 5:

        title = input("Enter Book Title : ")

        found = False

        dict_items = list(library.items())

        for item in dict_items:

            if item[1]["title"].lower() == title.lower():

                print(item[0], item[1])
                found = True
                break

        if found == False:
            print("Book Not Found")

    # --------------------------------------------------
    # Update copies

    elif choice == 6:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            copies = int(input("Enter New Copies : "))
            library[book_id]["copies"] = copies

            print("Copies Updated")

        else:
            print("Book Not Found")

    # --------------------------------------------------
    # Issue book

    elif choice == 7:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            if library[book_id]["copies"] > 0:

                library[book_id]["copies"] -= 1
                print("Book Issued")

            else:
                print("Book Not Available")

        else:
            print("Book Not Found")

    # --------------------------------------------------
    # Return book

    elif choice == 8:

        book_id = input("Enter Book ID : ")

        if book_id in library:

            library[book_id]["copies"] += 1
            print("Book Returned")

        else:
            print("Book Not Found")

    # --------------------------------------------------
    # Books with fewer than 3 copies

    elif choice == 9:

        print("\nBooks With Less Than 3 Copies")

        dict_items = list(library.items())

        for item in dict_items:

            if item[1]["copies"] < 3:
                print(item[1]["title"])

    # --------------------------------------------------
    # Unavailable books

    elif choice == 10:

        print("\nUnavailable Books")

        dict_items = list(library.items())

        for item in dict_items:

            if item[1]["copies"] == 0:
                print(item[1]["title"])

    # --------------------------------------------------
    # Most available book

    elif choice == 11:

        dict_items = list(library.items())

        max_book = dict_items[0][0]
        max_copies = dict_items[0][1]["copies"]

        for item in dict_items:

            if item[1]["copies"] > max_copies:

                max_book = item[0]
                max_copies = item[1]["copies"]

        print("\nMost Available Book")
        print(max_book, ":", max_copies)

    # --------------------------------------------------
    # Restocking report

    elif choice == 12:

        print("\nRestocking Report")

        dict_items = list(library.items())

        for item in dict_items:

            if item[1]["copies"] < 3:
                print(item[0], "-", item[1]["title"])

    # --------------------------------------------------
    # Immediate purchase dictionary

    elif choice == 13:

        purchase = {}

        dict_items = list(library.items())

        for item in dict_items:

            if item[1]["copies"] <= 1:
                purchase[item[0]] = item[1]

        print("\nBooks Requiring Immediate Purchase")
        print(purchase)

    # --------------------------------------------------
    # Library Summary Report

    elif choice == 14:

        total_books = 0
        unavailable = 0

        dict_items = list(library.items())

        for item in dict_items:

            total_books += item[1]["copies"]

            if item[1]["copies"] == 0:
                unavailable += 1

        print("\n===== LIBRARY SUMMARY REPORT =====")
        print("Total Titles :", len(library))
        print("Total Copies :", total_books)
        print("Unavailable Books :", unavailable)

    # --------------------------------------------------
    # Exit

    elif choice == 15:

        print("Program Ended")
        break

    else:
        print("Invalid Choice")

        