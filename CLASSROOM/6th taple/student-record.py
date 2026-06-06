#student id
#student name
#corce name
#fees paid
#store the above details in a list and display the details of the student
#1display the details of the student
#2display the first student details
#3display the last student details using negative indexing
#4to display only the studend id and name of the student
#5to display the count of all the students
#6to check if student name rahul exist in the list or not 

#creating student data
student = (                       
(101, "Rahul", "python", 25000),
(102, "Anjali", "java", 30000),
(103, "Suresh", "c++", 20000),
(104, "Priya", "python", 25000),
(105, "Amit", "java", 30000)
)
#------------------------------------------------------
#TASK 1: TO display all student records 
print("All student details:")
for record in student:
    print("student id:", record[0])
    print("student name:", record[1])
    print("course name:", record[2])
    print("fees paid:", record[3])
    print("-----------------------------")
#-------------------------------------------------------
#TASK 2: TO display the first student details
print("First student details:")
print("student id:", student[0][0])
print("student name:", student[0][1])
print("course name:", student[0][2])
print("fees paid:", student[0][3])
print("-----------------------------")
#-------------------------------------------------------
#TASK 3: TO display the last student details using negative indexing
print("Last student details:")
print("student id:", student[-1][0])
print("student name:", student[-1][1])
print("course name:", student[-1][2])
print("fees paid:", student[-1][3])
print("-----------------------------")
#-------------------------------------------------------
#TASK 4: TO display only the student id and name of the student
print("Student id and name:")
for record in student:
    print("student id:", record[0], "student name:", record[1]) 
print("-----------------------------")
#-------------------------------------------------------
#TASK 5: TO display the count of all the students
print("Total number of students:", len(student))
print("-----------------------------")
#-------------------------------------------------------
#TASK 6: TO check if student name rahul exist in the list or not
count = 0
for record in student:
    if record[1]== "Rahul":
        count += 1
if count > 0:
    print("Student name 'Rahul' exists in the list.")
else:
    print("Student name 'Rahul' does not exist in the list.")