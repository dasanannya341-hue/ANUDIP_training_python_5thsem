# Create a dictionary to store students' data
students = {
    'std101': 'Akash',
    'std102': 'Abhinav',
    'std103': 'Anil',
    'std104': 'Rahul'
}

# Display original data
print("Student Details:")
print(students)
print("-" * 50)

# Update existing student record
students['std103'] = 'Rohit'

# Add a new student record
students['std105'] = 'Rakesh'

# Display updated data
print("Updated Student Details:")
print(students)
print("-" * 50)

# Display records one by one
print("Roll No -> Student Name")
for roll_no in students:
    print(roll_no, "->", students[roll_no])