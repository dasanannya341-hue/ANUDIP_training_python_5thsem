'''3. Student Result Processing System 
Problem Statement 
Student marks are stored in results.txt. 
File Format 
S101,Anuj,85 
S102,Rahul,72 
S103,Priya,96 
S104,Neha,68 
S105,Amit,39 
S106,Sneha,54 
S107,Karan,91 
S108,Pooja,78 
S109,Rohit,47 
S110,Anjali,88 
Requirements 
Write a program to: 
1. Display all student records.  
2. Search a student using Student ID.  
3. Find topper and lowest scorer.  
4. Calculate class average.  
5. Count pass and fail students.  
6. Generate grades:  
o A (90+)  
o B (75–89)  
o C (40–74)  
o F (<40)  
7. Write grade reports into a new file named grades.txt. '''

# Function to display all student records
def display_records():
    file = open("results.txt", "r")
    data = file.readlines()

    print("\nStudent Records")
    for line in data:
        print(line.strip())

    file.close()


# Function to search student by ID
def search_student():
    student_id = input("Enter Student ID: ")

    file = open("results.txt", "r")
    data = file.readlines()

    found = False

    for line in data:
        details = line.strip().split(",")

        if details[0] == student_id:
            print("\nStudent Found")
            print("ID :", details[0])
            print("Name :", details[1])
            print("Marks :", details[2])
            found = True
            break

    if found == False:
        print("Student not found")

    file.close()


# Function to find topper and lowest scorer
def topper_lowest():
    file = open("results.txt", "r")
    data = file.readlines()

    topper = data[0].strip().split(",")
    lowest = data[0].strip().split(",")

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) > int(topper[2]):
            topper = details

        if int(details[2]) < int(lowest[2]):
            lowest = details

    print("\nTopper")
    print(topper[0], topper[1], topper[2])

    print("\nLowest Scorer")
    print(lowest[0], lowest[1], lowest[2])

    file.close()


# Function to calculate class average
def class_average():
    file = open("results.txt", "r")
    data = file.readlines()

    total = 0
    count = 0

    for line in data:
        details = line.strip().split(",")
        total += int(details[2])
        count += 1

    print("Class Average =", total / count)

    file.close()


# Function to count pass and fail students
def pass_fail():
    file = open("results.txt", "r")
    data = file.readlines()

    pass_count = 0
    fail_count = 0

    for line in data:
        details = line.strip().split(",")

        if int(details[2]) >= 40:
            pass_count += 1
        else:
            fail_count += 1

    print("Pass Students =", pass_count)
    print("Fail Students =", fail_count)

    file.close()


# Function to generate grades and write into grades.txt
def generate_grades():
    file = open("results.txt", "r")
    data = file.readlines()
    file.close()

    grade_file = open("grades.txt", "w")

    print("\nGrade Report")

    for line in data:
        details = line.strip().split(",")

        marks = int(details[2])

        if marks >= 90:
            grade = "A"
        elif marks >= 75:
            grade = "B"
        elif marks >= 40:
            grade = "C"
        else:
            grade = "F"

        report = details[0] + "," + details[1] + "," + str(marks) + "," + grade

        print(report)
        grade_file.write(report + "\n")

    grade_file.close()

    print("\nGrades written to grades.txt successfully")


# Main Program
while True:

    print("\n===== Student Result Processing System =====")
    print("1. Display All Student Records")
    print("2. Search Student")
    print("3. Topper and Lowest Scorer")
    print("4. Class Average")
    print("5. Pass and Fail Count")
    print("6. Generate Grades")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_records()

    elif choice == 2:
        search_student()

    elif choice == 3:
        topper_lowest()

    elif choice == 4:
        class_average()

    elif choice == 5:
        pass_fail()

    elif choice == 6:
        generate_grades()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")