'''Problem 2: Student Scholarship Evaluation System 
Problem Statement 
The marks obtained by students in the final examination are stored as follows: 
Sample Data 
marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 
Tasks 
1. Display students scoring above 85 marks.  
2. Find the topper.  
3. Find the student with the lowest marks.  
4. Calculate class average marks.  
5. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
6. Create a list of scholarship students (marks ≥ 90).  '''

marks = { 
    "Anuj": 92, 
    "Rahul": 76, 
    "Priya": 88, 
    "Neha": 64, 
    "Amit": 58, 
    "Sneha": 95, 
    "Karan": 81, 
    "Pooja": 73, 
    "Rohit": 47, 
    "Anjali": 90 
} 

#1. Display marks more than 85 .  
print("Display marks more than 85 ")
for item, num in marks.items():
    if num > 85 :
        print(item, num)


#2. Find the topper. 
hightet_marks=max(marks)
print("the highest-marks . ",hightet_marks ,(num))


#3. Find the student with the lowest marks.
lowest_marks = min(marks)
print("the lowest marks:", lowest_marks)

#4.Calculate class average marks.
total = 0

for mark in marks.values():
    total += mark

average = total / len(marks)

print("Class Average:", average)

# 5. Generate grades.
print("\nGrades:")

for student, mark in marks.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"

    print(student, ":", grade)

# 6. Create a list of scholarship students.
scholarship = []

for student, mark in marks.items():
    if mark >= 90:
        scholarship.append(student)

print("\nScholarship Students:", scholarship)