'''1. Employee Payroll Management System 
Problem Statement 
A company stores employee details in a text file named employees.txt. 
File Format 
EMP101,Anuj,45000 
EMP102,Rahul,52000 
EMP103,Priya,38000 
EMP104,Neha,61000 
EMP105,Amit,29000 
EMP106,Sneha,55000 
EMP107,Karan,47000 
EMP108,Pooja,72000 
EMP109,Rohit,33000 
EMP110,Anjali,68000 
Requirements 
Create a menu-driven program to: 
1. Display all employee records.  
2. Search employee details using Employee ID.  
3. Calculate the average salary.  
4. Find the highest-paid and lowest-paid employee.  
5. Display employees earning above ₹50,000.  
6. Add a new employee record to the file.  
7. Generate salary categories:  
o High (₹60,000 and above)  
o Medium (₹40,000–₹59,999)  
o Low (Below ₹40,000)  '''

# Function to display all employee records
def display_records():
    file = open("employees.txt", "r")
    data = file.readlines()

    print("\nEmployee Records")
    for line in data:
        print(line.strip())

    file.close()


# Function to search employee by ID
def search_employee():
    emp_id = input("Enter Employee ID: ")

    file = open("employees.txt", "r")
    data = file.readlines()

    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0] == emp_id:
            print("\nEmployee Found")
            print("ID:", details[0])
            print("Name:", details[1])
            print("Salary:", details[2])
            found = True
            break

    if found == False:
        print("Employee not found")

    file.close()


# Function to calculate average salary
def average_salary():
    file = open("employees.txt", "r")
    data = file.readlines()

    total = 0
    count = 0

    for line in data:
        details = line.strip().split(",")
        total += int(details[2])
        count += 1

    print("Average Salary =", total / count)

    file.close()


# Function to find highest and lowest paid employee
def highest_lowest():
    file = open("employees.txt", "r")
    data = file.readlines()

    highest = data[0].strip().split(",")
    lowest = data[0].strip().split(",")

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) > int(highest[2]):
            highest = details

        if int(details[2]) < int(lowest[2]):
            lowest = details

    print("\nHighest Paid Employee")
    print(highest[0], highest[1], highest[2])

    print("\nLowest Paid Employee")
    print(lowest[0], lowest[1], lowest[2])

    file.close()


# Function to display employees earning above 50000
def above_50000():
    file = open("employees.txt", "r")
    data = file.readlines()

    print("\nEmployees Earning Above 50000")

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) > 50000:
            print(details[0], details[1], details[2])

    file.close()


# Function to add a new employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    file = open("employees.txt", "a")
    file.write("\n" + emp_id + "," + name + "," + salary)
    file.close()

    print("Employee Added Successfully")


# Function to generate salary categories
def salary_category():
    file = open("employees.txt", "r")
    data = file.readlines()

    print("\nHigh Salary Employees")
    for line in data:
        details = line.strip().split(",")

        if int(details[2]) >= 60000:
            print(details[1], details[2])

    print("\nMedium Salary Employees")
    for line in data:
        details = line.strip().split(",")

        if int(details[2]) >= 40000 and int(details[2]) < 60000:
            print(details[1], details[2])

    print("\nLow Salary Employees")
    for line in data:
        details = line.strip().split(",")

        if int(details[2]) < 40000:
            print(details[1], details[2])

    file.close()


# Main Program
while True:

    print("\n===== Employee Payroll Management System =====")
    print("1. Display All Employees")
    print("2. Search Employee")
    print("3. Average Salary")
    print("4. Highest and Lowest Paid Employee")
    print("5. Employees Earning Above 50000")
    print("6. Add New Employee")
    print("7. Salary Categories")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        search_employee()

    elif choice == 3:
        average_salary()

    elif choice == 4:
        highest_lowest()

    elif choice == 5:
        above_50000()

    elif choice == 6:
        add_employee()

    elif choice == 7:
        salary_category()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")