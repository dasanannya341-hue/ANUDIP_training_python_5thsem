'''4. Mobile Contact Directory System 
Problem Statement 
Contacts are stored in contacts.txt. 
File Format 
Anuj,9876543210 
Rahul,9876543211 
Priya,9876543212 
Neha,9876543213 
Amit,9876543214 
Sneha,9876543215 
Karan,9876543216 
Pooja,9876543217 
Rohit,9876543218 
Anjali,9876543219 
Requirements 
Create a menu-driven application to: 
1. Display all contacts.  
2. Search a contact by name.  
3. Add a new contact.  
4. Update an existing contact number.  
5. Delete a contact.  
6. Display contacts whose names start with a vowel.  
7. Save all modifications back to the file. '''

# Function to display all contacts
def display_contacts():
    file = open("contacts.txt", "r")
    data = file.readlines()

    print("\nContact List")
    for line in data:
        print(line.strip())

    file.close()


# Function to search a contact
def search_contact():
    name = input("Enter name to search: ")

    file = open("contacts.txt", "r")
    data = file.readlines()

    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0].lower() == name.lower():
            print("\nContact Found")
            print("Name :", details[0])
            print("Number :", details[1])
            found = True
            break

    if found == False:
        print("Contact not found")

    file.close()


# Function to add a new contact
def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")

    file = open("contacts.txt", "a")
    file.write("\n" + name + "," + number)
    file.close()

    print("Contact Added Successfully")


# Function to update contact number
def update_contact():
    name = input("Enter contact name to update: ")

    file = open("contacts.txt", "r")
    data = file.readlines()
    file.close()

    new_data = []
    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0].lower() == name.lower():
            new_number = input("Enter new number: ")
            details[1] = new_number
            found = True

        new_data.append(",".join(details) + "\n")

    file = open("contacts.txt", "w")
    file.writelines(new_data)
    file.close()

    if found:
        print("Contact Updated Successfully")
    else:
        print("Contact not found")


# Function to delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ")

    file = open("contacts.txt", "r")
    data = file.readlines()
    file.close()

    new_data = []
    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0].lower() == name.lower():
            found = True
            continue

        new_data.append(line)

    file = open("contacts.txt", "w")
    file.writelines(new_data)
    file.close()

    if found:
        print("Contact Deleted Successfully")
    else:
        print("Contact not found")


# Function to display contacts starting with vowel
def vowel_contacts():
    file = open("contacts.txt", "r")
    data = file.readlines()

    print("\nContacts Starting With Vowel")

    for line in data:
        details = line.strip().split(",")

        if details[0][0].lower() in "aeiou":
            print(details[0], details[1])

    file.close()


# Main Program
while True:

    print("\n===== Mobile Contact Directory System =====")
    print("1. Display All Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contacts Starting With Vowel")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_contacts()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        add_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        vowel_contacts()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")