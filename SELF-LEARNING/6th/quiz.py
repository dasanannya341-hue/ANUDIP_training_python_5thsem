'''Online Quiz Performance 
Sample Data 
quiz_scores = { 
    "S001": 18, 
    "S002": 12, 
    "S003": 9, 
    "S004": 20, 
    "S005": 14, 
    "S006": 7, 
    "S007": 16, 
    "S008": 10, 
    "S009": 19, 
    "S010": 13 
} 
(Quiz is out of 20 marks.) 
Tasks 
• Display students scoring 15 or above.  
• Count students scoring below 10.  
• Find the top performer.  
• Create a list of students who passed (≥ 10 marks).  
• Calculate the class average. '''

quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Students scoring 15 or above
print("Students Scoring 15 or Above:")
for student in quiz_scores:
    if quiz_scores[student] >= 15:
        print(student)

# Count students scoring below 10
count = 0

for student in quiz_scores:
    if quiz_scores[student] < 10:
        count += 1

print("\nStudents Scoring Below 10:", count)

# Top performer
highest = 0
top_student = ""

for student in quiz_scores:
    if quiz_scores[student] > highest:
        highest = quiz_scores[student]
        top_student = student

print("\nTop Performer:")
print(top_student, "(", highest, ")", sep="")

# Passed students
passed = []

for student in quiz_scores:
    if quiz_scores[student] >= 10:
        passed.append(student)

print("\nPassed Students:")
print(passed)

# Class average
total = 0
count = 0

for student in quiz_scores:
    total += quiz_scores[student]
    count += 1

average = total / count

print("\nClass Average:", average)