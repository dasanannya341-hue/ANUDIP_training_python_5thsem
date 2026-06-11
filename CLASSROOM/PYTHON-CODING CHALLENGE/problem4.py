'''Problem 4: School Report Card Generator 
Problem Statement 
Student marks are stored in marks.txt. 
Sample Input/Data (marks.txt) 
S101,Anuj,92 
S102,Rahul,76 
S103,Priya,88 
S104,Neha,45 
S105,Amit,58 
S106,Sneha,95 
S107,Karan,81 
S108,Pooja,73 
S109,Rohit,39 
S110,Anjali,90 
Tasks 
1. Calculate grades for all students.  
2. Generate a report card file report_card.txt.  
3. Display topper details.  
4. Count pass and fail students.  
5. Display students eligible for merit certificates (marks ≥ 90).  
Sample Output 
Topper: 
Sneha (95) 
 
Passed Students: 9 
Failed Students: 1 
 
Merit Certificate Holders: 
Anuj 
Sneha 
Anjali 
 
Report Cards Generated Successfully.'''
# 1. Read data from marks.txt
students = []

try:
    with open("marks.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 3:
                roll = parts[0]
                name = parts[1]
                marks = int(parts[2])
                students.append((roll, name, marks))
except FileNotFoundError:
    print("Error: marks.txt file not found.")
    exit()

# 2. Assign grades
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

# 3. Generate report_card.txt
try:
    with open("report_card.txt", "w") as file:
        file.write("SCHOOL REPORT CARD\n\n")

        for roll, name, marks in students:
            grade = get_grade(marks)
            file.write(f"{roll}, {name}, Marks: {marks}, Grade: {grade}\n")

    print("Report Cards Generated Successfully.\n")
except Exception as e:
    print("Error writing report file:", e)

# 4. Find topper
topper = None
max_marks = 0

for roll, name, marks in students:
    if marks > max_marks:
        max_marks = marks
        topper = (roll, name, marks)

print("Topper:")
print(f"{topper[1]} ({topper[2]})\n")

# 5. Count pass and fail students
passed = 0
failed = 0

for s in students:
    if s[2] >= 40:
        passed += 1
    else:
        failed += 1

print(f"Passed Students: {passed}")
print(f"Failed Students: {failed}\n")

# 6. Merit certificate holders (marks ≥ 90)
print("Merit Certificate Holders:")
for roll, name, marks in students:
    if marks >= 90:
        print(name)
