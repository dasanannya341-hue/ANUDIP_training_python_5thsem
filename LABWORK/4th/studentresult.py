#Accept marks of 5 subjects. Display: • Total Marks  • Percentage  • Grade  Grade Criteria: Percentage Grade >=90 A+ >=75 A >=60 B >=40 C <40 Fail Also display the number of subjects failed. 
#taking the marks of 5 subjects as input
s1=int(input("Enter marks for subject 1: "))
#validating the marks
if s1 < 0 or s1 > 100:
    print("Marks should be between 0 and 100.")
s2=int(input("Enter marks for subject 2: "))
#validating the marks
if s2 < 0 or s2 > 100:
    print("Marks should be between 0 and 100.")
s3=int(input("Enter marks for subject 3: "))
#validating the marks   
if s3 < 0 or s3 > 100:
    print("Marks should be between 0 and 100.")
s4=int(input("Enter marks for subject 4: "))
#validating the marks
if s4 < 0 or s4 > 100:
    print("Marks should be between 0 and 100.")
s5=int(input("Enter marks for subject 5: "))
#validating the marks
if s5 < 0 or s5 > 100:
    print("Marks should be between 0 and 100.")
#calculating total marks and percentage
total_marks = s1 + s2 + s3 + s4 + s5
percentage = (total_marks / 500) * 100
#determining the grade and counting failed subjects
failed_subjects = 0
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"
    failed_subjects = sum(1 for mark in [s1, s2, s3, s4, s5] if mark < 40)
#displaying the results
print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)
if grade == "Fail":
    print("Number of subjects failed:", failed_subjects)
    