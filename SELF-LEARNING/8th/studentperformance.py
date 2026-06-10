'''Mini Assignment: Dictionary in Python 
1. Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
• Nested Dictionaries  
• Dictionary Traversal  
• Searching  
• Aggregation  
• Report Generation  '''

students = {
    "Anuj": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 67,
    "Amit": 45,
    "Riya": 88,
    "Karan": 55,
    "Sneha": 95,
    "Arjun": 78,
    "Pooja": 62
}

# Create a list
dict_items = list(students.items())

# Display all students
print("Student Records :")

for item in dict_items:
    print(item[0], ":", item[1])

# --------------------------------------------------

# Students scoring above 80
print("\nStudents Scoring Above 80 :")

for item in dict_items:
    if item[1] > 80:
        print(item[0])

# --------------------------------------------------

# Count pass and fail students

pass_count = 0
fail_count = 0

for item in dict_items:

    if item[1] >= 50:
        pass_count += 1

    else:
        fail_count += 1

print("\nPass Students :", pass_count)
print("Fail Students :", fail_count)

# --------------------------------------------------

# Topper

top_student = dict_items[0][0]
top_marks = dict_items[0][1]

for item in dict_items:

    if item[1] > top_marks:
        top_student = item[0]
        top_marks = item[1]

print("\nTopper :", top_student, "(", top_marks, ")")

# --------------------------------------------------

# Lowest Scorer

lowest_student = dict_items[0][0]
lowest_marks = dict_items[0][1]

for item in dict_items:

    if item[1] < lowest_marks:
        lowest_student = item[0]
        lowest_marks = item[1]

print("\nLowest Scorer :", lowest_student, "(", lowest_marks, ")")

# --------------------------------------------------

# Class Average

total_marks = 0

for item in dict_items:
    total_marks += item[1]

average_marks = total_marks / len(dict_items)

print("\nClass Average :", average_marks)

# --------------------------------------------------

# Students Above Average

print("\nStudents Above Average :")

for item in dict_items:
    if item[1] > average_marks:
        print(item[0])

# --------------------------------------------------

# Grade Lists

grade_A = []
grade_B = []
grade_C = []
grade_F = []

for item in dict_items:

    if item[1] >= 90:
        grade_A.append(item[0])

    elif item[1] >= 75:
        grade_B.append(item[0])

    elif item[1] >= 50:
        grade_C.append(item[0])

    else:
        grade_F.append(item[0])

print("\nGrade A :")
print(grade_A)

print("\nGrade B :")
print(grade_B)

print("\nGrade C :")
print(grade_C)

print("\nGrade F :")
print(grade_F)

# --------------------------------------------------

# Scholarship Students (marks > 85)

scholarship = []

for item in dict_items:

    if item[1] > 85:
        scholarship.append(item[0])

print("\nScholarship Students :")
print(scholarship)