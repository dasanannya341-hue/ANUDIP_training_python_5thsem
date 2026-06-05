#list of a student 
marks = [85, 90, 78, 92, 88]
passed=[]
merit=[]
fail=0
#assume first element is the highest
highest_marks = marks[0]
lowest_marks = marks[0]
#Display all passed students (marks ≥ 40).  
for mark in marks:
    if mark >= 40:
        passed.append(mark)
#Count the number of failed students.  
    else:
        fail += 1
#marit list above 75
if mark >= 75:
    merit.append(mark)
#finding the highest marks and lowest marks
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark
#Display the highest and lowest marks.

print("Passed students marks: ", passed)
print("Merit students marks: ", merit)
print("Number of failed students: ", fail)
print("Highest marks: ", highest_marks)
print("Lowest marks: ", lowest_marks)
