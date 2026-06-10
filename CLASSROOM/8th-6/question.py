student_marks = { 
"Anuj": 85, 
"Rahul": 72, 
"Priya": 91, 
"Neha": 68, 
"Amit": 78 
}
print(student_marks["Priya"])
print(student_marks["Amit"])
student_marks["Rahul"]=80
print(student_marks["Rahul"])
print("Rohan" in student_marks)
print(student_marks.keys())
print(student_marks.items())
student_marks['Rohan'] = 88
del student_marks["Neha"]
print(student_marks)